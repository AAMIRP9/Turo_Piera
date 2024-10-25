import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Turo Match Stats dataset
df = pd.read_csv('Data/Turo Match Stats.csv')

# Add matchweek filter
matchweek = st.sidebar.selectbox('Select Matchweek', df['Matchweek'].unique())
match_data = df[df['Matchweek'] == matchweek]

# Create a two-column layout for the possession and passing stats
col1, col2 = st.columns(2)

# First column: Possession stats (donut chart)
with col1:
    st.subheader("Possession Stats")
    home_possession = match_data['Home Team Possession'].values[0]
    away_possession = match_data['Away Team Possession '].values[0]

    fig1, ax1 = plt.subplots(figsize=(7, 7))  # Make the figure larger
    wedges, _, autotexts = ax1.pie(
        [home_possession, away_possession],
        autopct='%1.1f%%',
        colors=['#1d8313', '#fa0202'],
        startangle=90,
        pctdistance=1.2  # Move percentage values outside
    )
    ax1.add_artist(plt.Circle((0, 0), 0.7, color='white'))  # Create the donut hole

    # Increase font size of the values outside the donut chart
    for autotext in autotexts:
        autotext.set_fontsize(16)
        autotext.set_color("black")

    # Add legend instead of labels in the pie chart
    ax1.legend(wedges, [match_data['Home Team'].values[0], match_data['Away Team'].values[0]],
               title="Teams", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    ax1.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    st.pyplot(fig1)

# Second column: Passing stats (bar chart)
with col2:
    st.subheader("Passing Stats")
    home_passes = match_data['Home Team Passes '].values[0]
    away_passes = match_data['Away Team Passes'].values[0]

    fig2, ax2 = plt.subplots(figsize=(7, 7))  # Make the figure larger
    teams = [match_data['Home Team'].values[0], match_data['Away Team'].values[0]]
    passes = [home_passes, away_passes]

    bars = ax2.bar(teams, passes, color=['#1d8313', '#fa0202'], width=0.4)  # Skinnier bars with custom colors
    ax2.set_ylabel("Number of Passes", fontsize=14)

    # Remove box around the plot
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)

    # Add markers at the top of each bar with larger font size
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, yval + 5, int(yval), ha='center', va='bottom', fontsize=16)

    # Add legend to the bar chart
    ax2.legend(bars, [match_data['Home Team'].values[0], match_data['Away Team'].values[0]], title="Teams")

    st.pyplot(fig2)
    
    
    

# --- Loss of Possession Section ---

from mplsoccer import Pitch

# --- Load the Loss of Possession dataset as df_1 ---
df_1 = pd.read_csv('Data/merged_dataset.csv')

# Convert position columns to numeric and scale for pitch dimensions
df_1['X'] = pd.to_numeric(df_1['X'], errors='coerce') * 1.2
df_1['Y'] = pd.to_numeric(df_1['Y'], errors='coerce') * 0.8
df_1['X2'] = pd.to_numeric(df_1['X2'], errors='coerce') * 1.2
df_1['Y2'] = pd.to_numeric(df_1['Y2'], errors='coerce') * 0.8

# Function to create the loss of possession map
def create_loss_of_possession_map(df_1, team_name, matchweek):
    # Filter the data for the specific team, matchweek, and 'Loss of Possession' events
    team_data = df_1[
        (df_1['Team'] == team_name) & 
        (df_1['Matchweek'] == matchweek) & 
        (df_1['Event'] == 'Loss of Possession')
    ]

    # Set up the pitch
    fig, ax = plt.subplots(figsize=(13.5, 8))
    fig.set_facecolor('#1b893d')  # Light green for pitch background
    ax.patch.set_facecolor('#1b893d')
    
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#1b893d', line_color='#ffffff', stripe=True, stripe_color='#186d32')
    pitch.draw(ax=ax)

    plt.tight_layout()

    # Plot loss of possession events with red markers and lines
    for i in range(len(team_data)):
        plt.plot(
            (team_data.iloc[i]['X'], team_data.iloc[i]['X2']),
            (team_data.iloc[i]['Y'], team_data.iloc[i]['Y2']),
            color='#fa0202', linewidth=2, alpha=0.7
        )
        plt.scatter(
            team_data.iloc[i]['X'], team_data.iloc[i]['Y'], 
            color='#fa0202', s=500, edgecolor='#000000', zorder=3
        )
        plt.text(
            team_data.iloc[i]['X'], team_data.iloc[i]['Y'], 
            str(team_data.iloc[i]['Player']), 
            color='#ffffff', fontsize=12, ha='center', va='center', zorder=4
        )

    # Add title for the team's loss of possession map
    plt.title(f'{team_name} Loss of Possession Map for Matchweek {matchweek}', color='#ffffff', size=25)

    # Show the plot in Streamlit
    st.pyplot(fig)

# Streamlit app layout for the Loss of Possession Map
st.title('Loss of Possession Map')

# Sidebar for selecting matchweek and team

# Step 1: Matchweek filter (should reference the matchweek filter from previous sections)
matchweek_options = df['Matchweek'].unique()  # Assuming df holds the matchweek filter
selected_matchweek = st.sidebar.selectbox("Select a Matchweek (LoP Map)", matchweek_options)

# Step 2: Filter teams based on the selected matchweek
team_options = df_1[df_1['Matchweek'] == selected_matchweek]['Team'].unique()
selected_team = st.sidebar.selectbox("Select Team (LoP Map)", team_options)

# Display the loss of possession map for the selected team and matchweek
if selected_team and selected_matchweek:
    st.write(f"Displaying Loss of Possession Map for {selected_team} in Matchweek {selected_matchweek}")
    create_loss_of_possession_map(df_1, selected_team, selected_matchweek)

import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# --- Titles & Text ---

st.title("Clearances")

st.markdown("""
Explore the defensive contributions of teams by visualizing tackles made during the match.
""")
st.write("")
st.markdown("""
Use the matchweek and team filters to examine tackle locations on the pitch.
""")

# --- Dataset & Pitch Parameters ---

df = pd.read_csv('Data/merged_dataset.csv')

df['X'] = pd.to_numeric(df['X'], errors='coerce')
df['Y'] = pd.to_numeric(df['Y'], errors='coerce')
df['X2'] = pd.to_numeric(df['X2'], errors='coerce')
df['Y2'] = pd.to_numeric(df['Y2'], errors='coerce')

df['X'] = df['X'] * 1.2  
df['Y'] = df['Y'] * 0.8
df['endX'] = df['X2'] * 1.2
df['endY'] = df['Y2'] * 0.8

# Function to create the tackle map
def create_clearance_map(df, team_name, matchweek):
    # Filter the data for the specific team, matchweek, and 'Clearance' events
    team_data = df[(df['Team'] == team_name) & (df['Matchweek'] == matchweek) & (df['Event'] == 'Clearance')]

    # Set up the pitch
    fig, ax = plt.subplots(figsize=(13.5, 8))
    fig.set_facecolor('#1b893d')  # Light green for pitch background
    ax.patch.set_facecolor('#1b893d')
    
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#1b893d', line_color='#ffffff', stripe=True, stripe_color='#186d32')
    pitch.draw(ax=ax)

    plt.tight_layout()

    # Plot clearances with player numbers and larger markers
    for i in range(len(team_data)):
        plt.plot(
            (team_data.iloc[i]['X'], team_data.iloc[i]['endX']),
            (team_data.iloc[i]['Y'], team_data.iloc[i]['endY']),
            color='#bb1658', linewidth=2, alpha=0.7
        )
        plt.scatter(
            team_data.iloc[i]['X'], team_data.iloc[i]['Y'], 
            color='#bb1658', s=500, edgecolor='#ffffff', zorder=3  
        )
        plt.text(
            team_data.iloc[i]['X'], team_data.iloc[i]['Y'], 
            str(team_data.iloc[i]['Player']), 
            color='#ffffff', fontsize=12, ha='center', va='center', zorder=4  # Player number inside the circle
        )

    # Add title for the team's clearance map
    plt.title(f'{team_name} Clearance Map for {matchweek}', color='#ffffff', size=25)

    # Show the plot
    st.pyplot(fig)

# Streamlit app layout
st.title('Clearance Maps')

# Sidebar for selecting matchweek and team

# Step 1: Matchweek filter
matchweek_options = df['Matchweek'].unique()
selected_matchweek = st.sidebar.selectbox("Select a Matchweek", matchweek_options)

# Step 2: Filter teams based on the selected matchweek
team_options = df[df['Matchweek'] == selected_matchweek]['Team'].unique()
selected_team = st.sidebar.selectbox("Select Team", team_options)

# Display the clearance map for the selected team and matchweek
if selected_team and selected_matchweek:
    st.write(f"Displaying Shot map for {selected_team} in {selected_matchweek}")
    create_clearance_map(df, selected_team, selected_matchweek)

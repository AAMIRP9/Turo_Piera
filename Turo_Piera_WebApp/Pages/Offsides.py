import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# --- Titles & Text ---

st.title("Tackles")

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

df['X'] = df['X'] * 1.2  # Scale X coordinate
df['Y'] = df['Y'] * 0.8  # Scale Y coordinate

# Function to create the tackle map
def create_tackle_map(df, team_name, matchweek):
    # Filter the data for the specific team, matchweek, and 'Tackle' events
    team_data = df[(df['Team'] == team_name) & (df['Matchweek'] == matchweek) & (df['Event'] == 'Offside')]

    # Set up the pitch with dark green and light green stripes
    fig, ax = plt.subplots(figsize=(13.5, 8))
    fig.set_facecolor('#1b893d')  # Light green for pitch background
    ax.patch.set_facecolor('#1b893d')  # Pitch light green background

    # Realistic-looking pitch with white lines and green stripes
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#1b893d', line_color='#ffffff', stripe=True, stripe_color='#186d32')
    pitch.draw(ax=ax)

    plt.tight_layout()

    # Plot tackles with larger markers and player numbers
    for i in range(len(team_data)):
        # Tackles will have bright visible colors
        plt.scatter(
            team_data.iloc[i]['X'], team_data.iloc[i]['Y'], 
            color='#7b00ff', s=500, edgecolor='#ffffff', zorder=3  # Red-orange color for visibility with black edges
        )
        plt.text(
            team_data.iloc[i]['X'], team_data.iloc[i]['Y'], 
            str(team_data.iloc[i]['Player']), 
            color='#ffffff', fontsize=12, ha='center', va='center', zorder=4  # Black text inside the circle for high contrast
        )

    # Add title for the team's tackle map
    plt.title(f'{team_name} Tackle Map for {matchweek}', color='#ffffff', size=25)

    # Show the plot
    st.pyplot(fig)

# Streamlit app layout
st.title('Tackle Maps')

# Sidebar for selecting matchweek and team

# Step 1: Matchweek filter
matchweek_options = df['Matchweek'].unique()
selected_matchweek = st.sidebar.selectbox("Select a Matchweek", matchweek_options)

# Step 2: Filter teams based on the selected matchweek
team_options = df[df['Matchweek'] == selected_matchweek]['Team'].unique()
selected_team = st.sidebar.selectbox("Select a Team", team_options)

# Display the tackle map for the selected team and matchweek
if selected_team and selected_matchweek:
    st.write(f"Displaying tackle map for {selected_team} in Matchweek {selected_matchweek}")
    create_tackle_map(df, selected_team, selected_matchweek)
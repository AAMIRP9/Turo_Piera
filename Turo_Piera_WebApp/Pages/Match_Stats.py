import streamlit as st
import pandas as pd

# Page title and description
st.title("Match Stats")
st.markdown("""
View key match statistics, including passes, possession, fouls, and more. This page provides a comprehensive overview of both teams' performances in a selected matchweek.
Select the matchday to view match-specific stats and gain insights into team strategies and performance.
""")

# Custom CSS for styling
st.markdown("""
    <style>
    body { background-color: #f4f4f4; }
    .main-header { font-size:36px !important; color:#4CAF50 !important; text-align: center; }
    .result-pill {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #e0e0e0; /* Light grey pill background */
        border-radius: 50px;  /* Rounded corners for pill shape */
        padding: 15px 30px;  /* Padding for pill effect */
        font-size: 40px;  /* Increase font size for match result */
        font-weight: bold;
        color: black;  /* Black for team names and hyphen */
        margin-bottom: 20px; /* Space below pill */
    }
    .result-team {
        color: black;
        font-weight: bold;
        margin: 0 10px;
    }
    .result-hyphen {
        color: black;
        font-size: 40px; 
        margin: 0 20px;  /* Center hyphen with space */
    }
    .team-title { font-size: 24px; font-weight: bold; color: #4CAF50; text-align: center; }
    .metrics-title { font-size: 24px; font-weight: bold; color: transparent; text-align: center; }
    .team-value { font-size: 24px; font-weight: bold; color: red; text-align: center; }
    .metrics-value { font-size: 24px; color: black; text-align: center; }
    </style>
    """, 
    unsafe_allow_html=True
)

# Load Turo Match Stats dataset
df = pd.read_csv('Data/Turo Match Stats.csv')

# Matchweek filter
matchweek = st.sidebar.selectbox('Select Matchweek', df['Matchweek'].unique())
match_data = df[df['Matchweek'] == matchweek]

# Extract team names and goals
home_team = match_data['Home Team'].values[0]
away_team = match_data['Away Team'].values[0]
home_goals = match_data['Home Team Goals'].values[0]
away_goals = match_data['Away Team Goals'].values[0]

# Display match result in a pill shape
st.markdown(f"""
<div class="result-pill">
    <span class="result-team">{home_team} {home_goals}</span>
    <span class="result-hyphen">-</span>
    <span class="result-team">{away_goals} {away_team}</span>
</div>
""", unsafe_allow_html=True)

# Two columns for team stats with metrics in the center column
col1, col2, col3 = st.columns([1, 1, 1])

# Team stats lists for home and away team
stats = [
    ("Goals", home_goals, away_goals),
    ("Shots", match_data['Home Team Shots '].values[0], match_data['Away Team Shots'].values[0]),
    ("xG", match_data['Home Team xG'].values[0], match_data['Away Team xG'].values[0]),
    ("Possession", f"{match_data['Home Team Possession'].values[0]}%", f"{match_data['Away Team Possession '].values[0]}%"),
    ("Tackles", match_data['Home Team Tackles'].values[0], match_data['Away Team Tackles '].values[0]),
    ("Passes", match_data['Home Team Passes '].values[0], match_data['Away Team Passes'].values[0]),
    ("Fouls", match_data['Home Team Fouls'].values[0], match_data['Away Team Fouls'].values[0]),
    ("Clearances", match_data['Home Team Clearances '].values[0], match_data['Away Team Clearances '].values[0]),
    ("Offsides", match_data['Home Team Offsides '].values[0], match_data['Away Team Offsides '].values[0]),
    ("Saves", match_data['Home Team Saves '].values[0], match_data['Away Team Saves '].values[0]),
    ("Freekicks", match_data['Home Team Freekicks '].values[0], match_data['Away Team Freekicks '].values[0]),
    ("Corners", int(match_data['Home Team Corners'].values[0]), int(match_data['Away Team Corners '].values[0])),
    ("Loss of Possession", int(match_data['Home Team Loss of Possession '].values[0]), int(match_data['Away Team Loss of Possession '].values[0]))
]

# Display team stats side by side
with col1:
    st.markdown(f"<div class='team-title'>{home_team}</div>", unsafe_allow_html=True)
    for stat_name, home_value, _ in stats:
        st.markdown(f"<div class='team-value'>{home_value}</div>", 
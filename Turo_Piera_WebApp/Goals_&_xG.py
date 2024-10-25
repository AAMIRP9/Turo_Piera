import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Page title and description
st.title("Goals & xG")
st.markdown("""
Analyze the goals scored, expected goals (xG), and other key metrics related to goal-scoring chances. Compare actual goals with expected performance.
""")
st.write("")
st.markdown("""
Filter by matchweek and team to explore goal opportunities and xG for the selected match.
""")

# Load dataset
df = pd.read_csv('Data/Turo Shooting Data.csv')

# Matchweek filter
matchweek = st.sidebar.selectbox('Select Matchweek', df['Macthweek'].unique())

# Filter the dataset based on the selected matchweek
match_data = df[df['Macthweek'] == matchweek]

# Separate data for each team in the filtered match
team1 = match_data['Player Team'].unique()[0]
team2 = match_data['Player Team'].unique()[1]

team1_data = match_data[match_data['Player Team'] == team1]
team2_data = match_data[match_data['Player Team'] == team2]

# Extract minutes and cumulative xG for each team
team1_min = team1_data['Min']
team1_cumulative_xG = team1_data['xG'].cumsum()

team2_min = team2_data['Min']
team2_cumulative_xG = team2_data['xG'].cumsum()

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
fig.set_facecolor('#ffffff')  # Background color of the figure
ax.patch.set_facecolor('#ffffff')  # Background color of the plot

# Configure matplotlib styling
mpl.rcParams['xtick.color'] = '#000000'
mpl.rcParams['ytick.color'] = '#000000'

# Set up grid and axes
ax.grid(ls='dotted', lw=0.5, color='#000000', axis='y', zorder=1)
for spine in ['top', 'bottom', 'left', 'right']:
    ax.spines[spine].set_visible(False)

# Axis labels with customized fonts and colors
plt.xticks([0, 15, 30, 45, 60, 75, 90])
plt.xlabel('Minute', color='#000000', fontsize=16)
plt.ylabel('Cumulative xG', color='#000000', fontsize=16)

# Team 1: Green line for cumulative xG
ax.step(x=team1_min, y=team1_cumulative_xG, color='#4CAF50', label=team1, linewidth=4, where='post', zorder=3)

# Team 2: Red line for cumulative xG
ax.step(x=team2_min, y=t
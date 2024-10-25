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

# Function to create the tackle
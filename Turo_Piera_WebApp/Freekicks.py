import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# --- Titles & Text ---

st.title("Freekicks")

st.markdown("""
Explore the defensive contributions of teams by visualizing tackles made during the match.
""")
st.write("")
st.markdown("""
Use the matchweek and team filters to examine tackle locations on the pitch.
""")

# --- Dataset & Pitch Parameters ---

df = pd.read_csv('Data/merged_data
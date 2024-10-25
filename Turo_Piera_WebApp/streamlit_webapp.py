import streamlit as st 
import pandas as pd
from mplsoccer import VerticalPitch
import matplotlib.pyplot as plt 
from mplsoccer.pitch import Pitch
import seaborn as sns 
from PIL import Image 
import matplotlib.offsetbox as offsetbox 

# --- PAGE SETUP ---

home = st.Page(
    page="Home.py",
    title="Home", 
    icon=":material/home:",
    default=True,
)

match_stats = st.Page(
    page="Match_Stats.py",
    title="Match Stats",
    icon=":material/query_stats:",
)

Possession = st.Page(
    page="Possession.py",
    title="Possession",
    icon=":material/sports_soccer:",
)

goals_and_xg = st.Page(
    page="Goals_&_xG.py",
    title="Goals & xG",
    icon=":material/sports_soccer:",
)

shooting = st.Page(
    page="Shooting.py",
    title="Shooting",
    icon=":material/sports_soccer:",
)

tackles = st.Page(
    page="Tackles.py",
    title="Tackles",
    icon=":material/sports_soccer:",
)

clearances = st.Page(
    page="Clearances.py",
    title="Clearances",
    icon=":material/sports_soccer:",
)

freekicks = st.Page(
    page="Freekicks.py",
    title="Freekicks",
    icon=":material/sports_soccer:",
)

fouls = st.Page(
    page="Fouls.py",
    title="Fouls",
    icon=":material/sports_soccer:",
)

saves = st.Page(
    page="Saves.py",
    title="Saves",
    icon=":material/sports_soccer:",
)

offsides = st.Page(
    page="Offsides.py",
    title="Offsides",
    icon=":material/sports_soccer:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[home, match_stats, Possession, goals_and_xg, shooting, tackles, clearances, fouls, freekicks, saves, offsides])

# 

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# Team Logo
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio to change spacing

with col1:
    st.write("")  # Empty write to create space

with col2:
    logo_path = "Assets/Turo Peira Logo.png"  # Path to the logo image
    st.image(logo_path, width=300)  # Display the image

with col3:
    st.write("")  # Empty write to create space

# Define translations for the home page
home_translations = {
    "Español": {
        "welcome_title": "¡Bienvenido a la aplicación web de datos de fútbol!",
        "description": "Selecciona tu idioma y explora los datos e información sobre fútbol.",
        "choose_language": "Elige tu idioma / Tria el teu idioma",
        "submit": "Enviar",
        "confirmation": "Has seleccionado {language}. Navega a otras páginas para ver el idioma aplicado."
    },
    "Català": {
        "welcome_title": "Benvingut a l'aplicació web de dades de futbol!",
        "description": "Selecciona el teu idioma i explora les dades i informació sobre el futbol.",
        "choose_language": "Tria el teu idioma / Elige tu idioma",
        "submit": "Enviar",
        "confirmation": "Has seleccionat {language}. Navega a altres pàgines per veure l'idioma aplicat."
    }
}

# Language selection dictionary (Español and Català)
languages = ["Español", "Català"]

# Language selection widget
selected_language = st.selectbox("Elige tu idioma / Tria el teu idioma", languages)

# Store the selected language in session state
if selected_language:
    st.session_state["selected_language"] = selected_language

# Retrieve the selected language from session state or default to Español
selected_language = st.session_state.get("selected_language", "Español")

# Access translations for the home page
translations = home_translations[selected_language]

# Display the content in the selected language
st.title(translations["welcome_title"])
st.write(translations["description"])

# Submit button
if st.button(translations["submit"]):
    st.write(translations["confirmation"].format(language=selected_language))




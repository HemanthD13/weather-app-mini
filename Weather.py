import streamlit as st
from modules.api_handler import fetch_weather_data
from modules.ui_components import display_weather

from modules.utils import fahrenheit, kelvin

def apply_styles():
    with open("assets/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def main():
    apply_styles()
    st.title("Weather App")
    city = st.text_input("ENTER NAME OF THE CITY", key="city_input")
    unit = st.selectbox("SELECT TEMPERATURE UNIT", ["Celsius", "Fahrenheit", "Kelvin"], key="unit_selectbox")
    
    if city:
        weather_data = fetch_weather_data(city)
        if weather_data:
            display_weather(weather_data, unit)
        else:
            st.error("Couldn't fetch weather data.")

if __name__ == "__main__":
    main()

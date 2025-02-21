# ui_components.py
import streamlit as st

"""
Module responsible for UI components of the Weather App.

Contains functions to display weather data in a structured format.
"""


def display_weather(weather_data):
    """
    Displays the weather data on the Streamlit app.

    Args:
        weather_data (dict): A dictionary containing weather data such as
                              temperature, humidity, weather description, and wind speed.
    """
    st.subheader(f"Weather in {weather_data['city']}")
    st.write(f"Temperature: {weather_data['temperature']}°C")
    st.write(f"Humidity: {weather_data['humidity']}%")
    st.write(f"Weather: {weather_data['weather_description']}")
    st.write(f"Wind Speed: {weather_data['wind_speed']} m/s")

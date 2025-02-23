import streamlit as st
from modules.utils import fahrenheit, kelvin

def display_weather(weather_data,unit):
    if weather_data:
        
        st.write(f"### Weather in {weather_data['city']}")
        if unit == "Fahrenheit":
            st.write(f"🌡️ **Temperature**: {fahrenheit(weather_data['temperature'])}°F")
        elif unit == "Kelvin":
            st.write(f"🌡️ **Temperature**: {kelvin(weather_data['temperature'])} K")
        else:
            st.write(f"🌡️ **Temperature**: {weather_data['temperature']}°C")
        st.write(f"💧 **Humidity**: {weather_data['humidity']}%")
        st.write(f"☁️ **Weather Description**: {weather_data['weather_description'].capitalize()}")
        st.write(f"🌬️ **Wind Speed**: {weather_data['wind_speed']} m/s")

    else:
        st.error("Failed to fetch weather data.")

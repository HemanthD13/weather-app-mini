import streamlit as st
from PIL import Image

# Add background images for different weather conditions
def get_weather_image(weather_description):
    """Returns the path to an image based on weather conditions."""
    if 'clear' in weather_description:
        return "images/sunny.jpg"
    elif 'cloud' in weather_description:
        return "images/cloudy1.jpg"
    elif 'rain' in weather_description:
        return "images/rainy.jpg"
    elif 'snow' in weather_description:
        return "images/snowy.jpg"
    else:
        return "images/haze.jpg"

def display_weather(weather_data):
    """Displays weather data in a user-friendly format."""
    if weather_data:
        # Get the appropriate weather image
        weather_image = get_weather_image(weather_data['weather_description'].lower())
        
        # Display the background image (cover the screen)
        st.image(weather_image, use_container_width=True)  # Updated parameter

        # Display weather information with better styling
        st.write(f"### Weather in {weather_data['city']}")
        st.write(f"🌡️ **Temperature**: {weather_data['temperature']}°C")
        st.write(f"💧 **Humidity**: {weather_data['humidity']}%")
        st.write(f"☁️ **Weather**: {weather_data['weather_description'].capitalize()}")
        st.write(f"🌬️ **Wind Speed**: {weather_data['wind_speed']} m/s")

    else:
        st.error("Failed to fetch weather data.")

import streamlit as st
from modules.api_handler import fetch_weather_data
from modules.ui_components import display_weather
from modules.utils import fahrenheit,kelvin

def apply_styles():
    """Apply custom CSS to improve UI."""
    st.markdown("""
        <style>
        body {
            background-color: #f0f0f0;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput>div>div>input {
            background-color: #e0e0e0;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }
        .stButton>button {
            background-color: #ff9800;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #e68900;
        }
        </style>
        """, unsafe_allow_html=True)

def main():
    apply_styles()  # Apply custom styles
    
    st.title("Weather App")
    
    # User input for the city
    city = st.text_input("Enter a city name", "")
    unit = st.selectbox("Select temperature unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if city:
        # Fetch weather data for the given city
        weather_data = fetch_weather_data(city)
        
        if weather_data:
            # Display weather data using the UI components module
            display_weather(weather_data, unit)
        else:
            st.error("Couldn't fetch weather data. Please try again.")
    
if __name__ == "__main__":
    main()
# import streamlit as st
# from modules.api_handler import fetch_weather_data
# from modules.ui_components import display_weather

# # Streamlit title and description
# st.title("Weather Application")
# st.write("Select a temperature unit and enter the city to get the weather data.")
# st.write("Select a temperature unit and enter the city to get the weather data.")
# # Dropdown menu for temperature selection
# unit = st.selectbox(
#     "Choose the unit to display the temperature:",
#     ("Celsius", "Fahrenheit", "Kelvin")
# )

# # User input for city name
# city = st.text_input("Enter the city name:", value="New York")

# # Fetch weather data
# if city:
#     weather_data = fetch_weather_data(city)
#     display_weather(weather_data, unit)

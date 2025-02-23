# Weather App

This app allows you to search for cities by name and view their weather details, including temperature, pressure, and humidity. You can also switch between temperature scales: Celsius, Kelvin, and Fahrenheit.

---

## To run the code on your local machine:

### Step 1: Get an API Key
1. Visit [OpenWeatherMap](https://openweathermap.org/api) and sign up for a free account.
2. Generate an API key from the dashboard after logging in.

### Step 2: Add API Key to Config
1. Inside the root folder of your project, create a file named `config.py`.
2. Add the following code to the `config.py` file to store the API key:

   ```python
   # config.py
   API_KEY = "YOUR_API_KEY_HERE"
Replace "YOUR_API_KEY_HERE" with the API key you obtained from OpenWeatherMap.

### Step 3: Install Dependencies
Ensure that you have Python 3.7 or later installed on your machine. Then, install the required dependencies using pip by running the following command:

```
 pip install -r requirements.
 ```
_The requirements.txt should include dependencies like streamlit, requests, and any other libraries your project requires._

### Step 4: Run the Application 
Run the app using Streamlit. From your terminal, navigate to your project folder and run:
```
streamlit run Weather.py
```
This will start the app locally and open it in your browser.


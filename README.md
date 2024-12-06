# Weather-Alert-System 🌦️    
# Stay Dry and Prepared with Real-time Weather Alerts! 🌂    
Welcome to the Weather Alert System! This Python-based application checks weather forecasts and sends SMS notifications if rain is expected, ensuring you never forget your umbrella again. This project integrates OpenWeatherMap for weather data and Twilio for sending SMS alerts.    

# Features ✨
• Location-Based Weather Forecast: Automatically fetches weather forecasts based on your address.
• Rain Alerts: Notifies you via SMS if rain is expected.
• Easy Setup: Simple configuration with environment variables for API keys and tokens.    
# How It Works ⚙️
1. Geocoding: Converts your address into geographical coordinates.
2. Weather Forecasting: Fetches weather data using OpenWeatherMap API.
3. Rain Detection: Checks if rain is forecasted in the next few hours.
4. SMS Notification: Sends an SMS alert using Twilio if rain is detected.

# Prerequisites 📋
• Python 3.x
• Twilio Account (for sending SMS)
• OpenWeatherMap API Key

# Installation 🚀
1. Clone the Repository:    
   git clone https://github.com/LukeShawket/weather-alert-system.git
   cd weather-alert-system
2. Install Dependencies:
   pip install -r requirements.txt
3. Set Up Environment Variables:
   export MY_OPEN_WEATHER_API_KEY='your_open_weather_api_key'
   export ACCOUNT_SID='your_twilio_account_sid'
   export AUTH_TOKEN='your_twilio_auth_token'
   
# Usage 🛠️
1. Edit the main.py file to include your address:
   MY_ADDRESS = "Your Address Here"
2. Run the application:
   bash
   python main.py

# Contribution 🌟
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

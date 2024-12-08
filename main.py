from geopy.geocoders import Nominatim
import requests
import os
from twilio.rest import Client

MY_OPEN_WEATHER_API_KEY = os.environ["My Open Weather Map API key"]
OPEN_WEATHER_END_POINT = "https://api.openweathermap.org/data/2.5/forecast"

ACCOUNT_SID = os.environ["My Twilio Account Sid"]
AUTH_TOKEN = os.environ["My Twilio Authorization Token"]

MY_ADDRESS = "Some address"

geolocater = Nominatim(user_agent="My_Locater")
my_location = geolocater.geocode(MY_ADDRESS)
my_latitude = my_location.latitude
my_longitude = my_location.longitude

weather_parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": MY_OPEN_WEATHER_API_KEY,
    "cnt": 4
}

response = requests.get(OPEN_WEATHER_END_POINT, params=weather_parameters)
response.raise_for_status()

need_umbrella = False

for i in range(4):
    weather_id = response.json()["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        need_umbrella = True

if need_umbrella:
    # twilio
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today, take the umbrella with you.",
        from_="Your twilio number",
        to="some phone number",
    )
    print(message.status)

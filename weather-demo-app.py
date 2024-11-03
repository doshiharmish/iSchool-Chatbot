#Importing all libraries
import streamlit as st
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

api_key = "302bd4579660ebde60eb8e5d21fdc719"  # Replace with your OpenWeatherMap API key
#creating functions
def get_lat_long(city_name):
    # Initialize Nominatim API with a unique user agent
    geolocator = Nominatim(user_agent="your_unique_user_agent_string_here")
    
    try:
        # Use geolocator to get the location
        location = geolocator.geocode(city_name)
        
        if location:
            # Extract latitude and longitude
            return location.latitude, location.longitude
        else:
            print("City not found.")
            return None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Error: {e}")
        return None

st.title("City Weather dashboard")
# User input for city name
city = st.text_input("Enter a city name")
if city:
    #fetching lat-long
    coordinates = get_lat_long(city)
    if coordinates:
        latitude = coordinates[0]
        longitude = coordinates[1]
        #Step 2: Fetch weather data using the obtained latitude and longitude
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
        weather_response = requests.get(weather_url)
        if weather_response.status_code == 200:
                weather_data = weather_response.json()
                temperature = weather_data["main"]["temp"]
                weather = weather_data["weather"][0]["description"]
                icon = weather_data["weather"][0]["icon"]
                
                # Display the weather information
                st.write(f"### Weather in {city.capitalize()}")
                st.write(f"Temperature: {temperature} °C")
                st.write(f"Condition: {weather.capitalize()}")
                st.image(f"http://openweathermap.org/img/wn/{icon}.png")
        else:
                st.error("Could not retrieve weather data.")
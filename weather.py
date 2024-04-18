import os, dotenv
from langchain_community.utilities import OpenWeatherMapAPIWrapper

dotenv.load_dotenv()
weather = OpenWeatherMapAPIWrapper()

def get_weather(location='Dhaka'):
    weather_data = weather.run(location)
    return weather_data

if __name__ == "__main__":
    wd = get_weather()
    print(wd)

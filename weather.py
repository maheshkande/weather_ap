import requests

def get_weather(city):
    api_key = "d034a7e76ab8d5ec370645dfe12b274c"  # Your API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city.strip().title(),   # Clean and format city name
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\n🌍 Weather in {data['name']}, {data['sys']['country']}:")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"☁️ Condition: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🍃 Wind Speed: {data['wind']['speed']} m/s\n")
    else:
        print(f"\n❌ Error {response.status_code}: {data.get('message', 'Something went wrong.')}\n")

# ----- Run the app -----
print("🔍 Live Weather App 🌦")
city_name = input("Enter a city name: ")
get_weather(city_name)

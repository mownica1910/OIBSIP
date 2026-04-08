import requests

API_KEY = "aa3c4607e77026d5d6134284284213bc"

city = input("Enter city name: ").strip()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if str(data.get("cod")) != "200":
    print("Error:", data.get("message"))
else:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\nWeather Details")
    print("City:", city.title())
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)
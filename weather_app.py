import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = '30d4741c779ba94c470ca1f63045390a'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")
        return None

def show_weather():
    city = city_entry.get()
    if city:
        weather_data = get_weather(city)
        if weather_data:
            weather_info = (
                f"City: {weather_data['name']}\n"
                f"Temperature: {weather_data['main']['temp']}°C\n"
                f"Weather: {weather_data['weather'][0]['description']}"
            )
            messagebox.showinfo("Weather Information", weather_info)
        else:
            messagebox.showerror("Error", "City not found or API limit reached.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Initialize the Tkinter application
app = tk.Tk()
app.title("Weather App")

# Create and place GUI elements
tk.Label(app, text="Enter City:").pack(pady=10)
city_entry = tk.Entry(app)
city_entry.pack(pady=5)

tk.Button(app, text="Get Weather", command=show_weather).pack(pady=20)

# Run the Tkinter event loop
app.mainloop()

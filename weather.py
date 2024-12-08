import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk  
def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            city_name = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            weather_info.set(f"City: {city_name}\nTemperature: {temperature}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", f"API Error: {data.get('message', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
def on_search_button_click():
    city = city_entry.get().strip()  
    if city:
        get_weather(city, "b4a199b4ed564ae0e73d3d697d889456")  
    else:
        messagebox.showerror("Input Error", "Please enter a city name.")
root = tk.Tk()
root.title("Weather App")
root.geometry("600x600")
root.resizable(False, False)
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(fill="both", expand=True)
try:
    
    background_image = Image.open("images/background.jpg")  
    background_image = background_image.resize((600, 600), Image.Resampling.LANCZOS)  
    background_image = ImageTk.PhotoImage(background_image)
    canvas.create_image(0, 0, anchor="nw", image=background_image)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load background image: {e}")
frame = tk.Frame(root, bg="white", bd=10, relief="solid", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame
instructions_label = tk.Label(frame, text="Enter city name to get weather info:", font=("Arial", 14), bg="white")
instructions_label.pack(pady=10)
city_entry = tk.Entry(frame, font=("Arial", 14), bd=2, relief="solid", width=20)
city_entry.pack(pady=10)
search_button = tk.Button(frame, text="Search", font=("Arial", 14), command=on_search_button_click, bg="#4CAF50", fg="white", bd=2, relief="solid")
search_button.pack(pady=10)
weather_info = tk.StringVar()
weather_info_label = tk.Label(frame, textvariable=weather_info, font=("Arial", 12), bg="white", justify="left")
weather_info_label.pack(pady=20)
root.mainloop()

from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    api_key = "5ebe36183f12b0f0ef9764dc144a1ca9"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url).json()

    if data.get("weather"):
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)))
        pressure_label1.config(text=data["main"]["pressure"])
        humidity_label1.config(text=data["main"]["humidity"])
        wind_speed = data["wind"]["speed"] * 3.6
        wind_label1.config(text=str(round(wind_speed, 2)))


        if "rain" in data.keys():
            precipitation_label1.config(text=f'{data["rain"]["1h"]} mm' if "1h" in data["rain"].keys() else "N/A")
        elif "snow" in data.keys():
            precipitation_label1.config(text=f'{data["snow"]["1h"]} mm' if "1h" in data["snow"].keys() else "N/A")
        else:
            precipitation_label1.config(text="N/A")
    else:
        w_label1.config(text="N/A")
        wb_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        pressure_label1.config(text="N/A")
        humidity_label1.config(text="N/A")
        wind_label1.config(text="N/A")
        precipitation_label1.config(text="N/A")



win = Tk()
win.title("Weather Forecasting")
win.config(bg="green")
win.geometry("570x700")

name_label = Label(win, text="Weather Forecasting App", font=("Helvetica", 30))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
    "National Capital Territory of Delhi", "Puducherry", "Patna", "Muzaffarpur"
]
com = ttk.Combobox(win, values=list_name, font=("Helvetica", 25), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather Climate", font=("Helvetica", 20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Helvetica", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Helvetica", 20))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", font=("Helvetica", 20))
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature (°C)", font=("Helvetica", 20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", font=("Helvetica", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

pressure_label = Label(win, text="Pressure (hPa)", font=("Helvetica", 20))
pressure_label.place(x=25, y=470, height=40, width=210)
pressure_label1 = Label(win, text="", font=("Helvetica", 20))
pressure_label1.place(x=250, y=470, height=40, width=210)

humidity_label = Label(win, text="Humidity (%)", font=("Helvetica", 20))
humidity_label.place(x=25, y=540, height=40, width=210)
humidity_label1 = Label(win, text="", font=("Helvetica", 20))
humidity_label1.place(x=250, y=540, height=40, width=210)

wind_label = Label(win, text="Wind Speed (km/h)", font=("Helvetica", 20))
wind_label.place(x=25, y=610, height=40, width=210)
wind_label1 = Label(win, text="", font=("Helvetica", 20))
wind_label1.place(x=250, y=610, height=40, width=210)

precipitation_label = Label(win, text="Precipitation (1h)", font=("Helvetica", 20))
precipitation_label.place(x=25, y=680, height=40, width=210)
precipitation_label1 = Label(win, text="", font=("Helvetica", 20))
precipitation_label1.place(x=250, y=680, height=40, width=210)

done_button = Button(win, text="Done", font=("Helvetica", 25), command=data_get)
done_button.place(x=375, y=190, height=50, width=100)

win.mainloop()

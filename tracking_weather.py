import requests
import pandas as pd
import matplotlib.pyplot as plt

# Cell 2
url = "https://2eraiuh.dlai.link/api/weather"
response = requests.get(url)
status = response.status_code
print(status)

# Cell 3
data = response.json()
print(type(data))

# Cell 4
print(data.keys())

# Cell 5
weather_data = data["data"]
weather_data.keys()

# Cell 6
df = pd.DataFrame(weather_data['weather'])
print(df)

# Cell 7
numeric_columns = ["mintempC", "maxtempC", "totalSnow_cm", "sunHour", "mintempF", "maxtempF", "uvIndex", "avgtempF", "avgtempC"]
df[numeric_columns] = df[numeric_columns].astype(float)
df["date"] = pd.to_datetime(df["date"])
df.set_index(df["date"], inplace=True)

# Cell 8
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["mintempC"], label="Min Temperature (°C)", marker="o", color="blue")
plt.plot(df.index, df["maxtempC"], label="Max Temperature (°C)", marker="o", color="red")
plt.title("Minimum and Maximum Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(df.index, df.index.strftime("%Y-%m-%d"))
plt.grid(True)
plt.legend()
plt.show()

# Cell 9
city = "Sydney"
url_wttr = f"http://wttr.in/{city}?format=j1"
response_wttr = requests.get(url_wttr)
weather_data = response_wttr.json()["data"]
df = pd.DataFrame(weather_data["weather"])
print(df.head())

# Cell 10
url_wttr_2 = f"http://wttr.in/{city}"
response_wttr_2 = requests.get(url_wttr_2)
print(response_wttr_2.text)
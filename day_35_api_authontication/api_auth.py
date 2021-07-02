import requests
import smtplib
import os
api_key = "0ab445ba8eb027253678307098fbb49c"
ID = 700

MY_LAT = 16.704987
MY_LAG = 74.243256
my_email = "your mail"
password = "your password"
parameter = {
    "lat" : MY_LAT,
     "lon" : MY_LAG,
     "appid" : api_key,
     "exclude":"current,minutely,daily"
      }
data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
hourly_data = data.json()["hourly"]
first_hour = hourly_data[0:12]
is_rain = False
#print(first_hour)
for hour_data in first_hour:
    condition_check = hour_data["weather"][0]["id"]
    if condition_check <= ID:
        is_rain = True
# if first_hour["weather"][0]["id"] < ID:
#     print("its rainy day")
is_rain=True
if is_rain:
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr=my_email, to_addrs=my_email, msg = "subject:RAIN TODAY\n\nbring an umbrella")

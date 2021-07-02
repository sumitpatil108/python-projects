import requests
import datetime
import time
import smtplib
MY_LAT = 16.704987
MY_LAG = 74.243256

def is_iss_overhead():
    data = requests.get("http://api.open-notify.org/iss-now.json")
    data.raise_for_status()
    iss_position = data.json()["iss_position"]
    iss_lat = float(iss_position["latitude"])
    iss_lag = float(iss_position["longitude"])
    if MY_LAT-5<= iss_lat <=MY_LAT+5 and MY_LAG-5 <=iss_lag <=MY_LAG+5:
        return True





#..................datatime
def is_night():
    parameter = {
        "lat":MY_LAT,
         "lng":MY_LAG,
         "formatted":0,
    }
    data = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    data.raise_for_status()
    #print(data.json())
    result = data.json()["results"]
    surnrise = int(result["sunrise"].split("T")[1].split(":")[0])
    sunset = int(result["sunset"].split("T")[1].split(":")[0])
    #sunset = str(sunset)
    #print(sunset.split("T")[1].split(":")[0])

    now = datetime.datetime.now()
    hour = now.hour
    if hour>=sunset and hour<=surnrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user="sppjain8055@gmail.com", password="sumitpatil1008108")
            conn.sendmail(from_addr="sppjain8055@gmail.com", to_addrs="sppjain8055@gmail.com",
                          msg="subject:LOOK UP👆👆\n\nthe iss is overhead look up sumit",
                          )
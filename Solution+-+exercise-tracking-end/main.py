import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 80.0
HEIGHT_CM = 167.0,
AGE = 21
#os.environ["age"] = "21"
print(os.getenv("age"))

APP_ID = "42847c3a"#os.environ["YOUR_APP_ID"]
API_KEY = "bef8e578c1dbf5c4870cdf069ee43e1a"#os.environ["YOUR_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e33792796a0909dc193619fd419718e2/copyOfMyWorkouts/workouts"#os.environ["YOUR_SHEET_ENDPOINT"]

#exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }
parameters = {
 "query":"ran 3 miles",
 "gender":"male",
 "weight_kg":80.5,
 "height_cm":167.64,
 "age":21
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    #Basic Auth
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         os.environ["USERNAME"],
    #         os.environ["PASSWORD"],
    #     )
    # )

    #Bearer Token
    # bearer_headers = {
    # "Authorization": f"Bearer {os.environ['TOKEN']}"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )

    print(sheet_response.text)
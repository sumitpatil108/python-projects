import requests
import datetime
USERNAME = "sampatil"
TOKAN = "jshjvghyefw5"

PIXAR_END_POINT = "https://pixe.la/v1/users"

parameter = {
   "token":"jshjvghyefw5",
    "username":"sampatil",
"agreeTermsOfService":"yes",
"notMinor":"yes"

}
# data = requests.post(PIXAR_END_POINT, json=parameter)
# print(data.text)

graph_endpoint = f"{PIXAR_END_POINT}/{USERNAME}/graphs"

body = {
 "id":"graph1",
"name":"Book Reading",
"unit":"hours",
"type":"float",
"color":"shibafu"
}
headers = {
    "X-USER-TOKEN":TOKAN
}
# data = requests.post(url=graph_endpoint, json=body, headers=headers)
# print(data.text)
#https://pixe.la/@sampatil
DATE = str(datetime.datetime.now()).split(" ")[0].replace("-","")
pixal_end_point =f"{graph_endpoint}/graph1"
pixal = {
    "date": DATE,
    "quantity":str(1)
}
# data_pixal = requests.post(url=pixal_end_point, json=pixal, headers=headers)
# print(data_pixal.text)
update_endpoint = f"{pixal_end_point}/{DATE}"
put = {
"quantity":str(2)
}

data = requests.put(url=update_endpoint, json=put, headers=headers)
print(data.text)
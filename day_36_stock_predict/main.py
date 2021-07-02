import requests
import smtplib
my_email = "my mail"
password = "my password"


stock_name = "TSLA"
COMPANY_NAME = "Tesla Inc"

tesla_news_api_key = "1fd692ed88034d74927ea74ebf0186f6"
tesla_market_api_key = "NHJWYDTQ6NMA1PEH"


api_end_point_tesla = "https://www.alphavantage.co/query"
api_end_point_tesla_news = "http://newsapi.org/v2/everything"

parameter = {
    "function": "TIME_SERIES_DAILY",
     "symbol":"IBM",
    "apikey": tesla_market_api_key

}
data = requests.get(api_end_point_tesla, params=parameter)
data.raise_for_status()
data = data.json()["Time Series (Daily)"]
#print(data.json()["Time Series (Daily)"]["2021-02-04"])
data_list = [value["4. close"] for (key,value) in data.items()]
#print(data_list)

yesterday_closing_price = data_list[0]
day_before_yesterday_closing_price = data_list[1]

difference = abs(float(day_before_yesterday_closing_price)-float(yesterday_closing_price))
print(difference)

diff_per = (difference / float(yesterday_closing_price)) * 100
print(diff_per)

if diff_per > 5:
    params = {
        "q" : "tesla" ,
    "apiKey": tesla_news_api_key,
    }
    data = requests.get(api_end_point_tesla_news, params=params)
    news_data = data.json()["articles"][:3]
    news_data_list = [f"HEADLINE: {data['title']} \ndescription: {data['description']}" for data in news_data ]
    for i in news_data_list:
        #print(i)
        i=i.encode('utf-8')
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"subject:TESLA STOCK INFO \n\n {i}")


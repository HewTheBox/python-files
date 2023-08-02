import requests
import  math
import datetime as dt


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

#get current date and time
current_date = dt.datetime(2023,3,4)
date_now = str(current_date.now()).split()
# yesterday = current_date.today()
yesterday = str((current_date.today() - dt.timedelta(days=1))).split()

# print(yesterday[0])
# print(date_now[0])


#parameters
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "D63SLGPSV9O5NBF2"
}

news_parameters = {
    "q": "tesla",
    # "domains": ["techcrunch.com", "thenextweb.com"],
    "from": yesterday[0],
    "to": date_now[0],
    "sortBy": "publishedAt",
    "apiKey": "34cf6e7f2f9f460f9fb5a28d36360bde",
    "qInTitle": COMPANY_NAME,
}




#requesting news data
news_update = requests.get("https://newsapi.org/v2/everything",params=news_parameters)
news_data = news_update.json()

articles  = news_data["articles"] #list
one_item = articles[0] # dict
# print(one_item)
for i in range(len(articles) -1):
    for key,value in articles[i].items():
        if (key == "title") or (value=="content"):
            # print("inside")
            if COMPANY_NAME in key or COMPANY_NAME in value:
                print("okay")
            else:
                # for line in articles[0]['content'].splitlines():
                #     print(line)
                conttent = articles[0]['content']
                message = f"Headline: {articles[0]['title']}\nBrief: {conttent}"
                
                
                
print(type(articles[0]['content']))
                            
#requesting stock data
stock_update = requests.get("https://www.alphavantage.co/query", params=parameters)
data = stock_update.json()
closed = data["Time Series (Daily)"]["2023-07-24"]["4. close"]
opened = data["Time Series (Daily)"]["2023-07-21"]["1. open"]

#calculating changes in price
change_in_price = float(closed) - float(opened)

if change_in_price > 0:
    print(f"TSLA: 🔺{math.floor(change_in_price)}%")
    print(message)
else:
    print(f"TSLA: 🔻{math.floor(change_in_price)}%")
    print(message)

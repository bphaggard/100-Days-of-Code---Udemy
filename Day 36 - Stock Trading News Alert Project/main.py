from datetime import datetime, timedelta
import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = os.environ.get("STOCK_API")
NEWS_API = os.environ.get("NEWS_API")

# DATETIME
yesterday = datetime.now() - timedelta(1)
before_yesterday = datetime.now() - timedelta(2)
date_yesterday = yesterday.strftime('%Y-%m-%d')
date_before_yesterday = before_yesterday.strftime('%Y-%m-%d')

# STOCK API
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API}"
stock_response = requests.get(stock_url)
stock_response.raise_for_status()
stock_data = stock_response.json()

# NEWS API
news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={date_yesterday}&sortBy=popularity&apiKey={NEWS_API}"
news_response = requests.get(news_url)
news_response.raise_for_status()
news_data = news_response.json()

# Comparing prices
def compare_close_price():
    yesterday_price = float(stock_data["Time Series (Daily)"][date_yesterday]["4. close"])
    before_yesterday_price = float(stock_data["Time Series (Daily)"][date_before_yesterday]["4. close"])
    if yesterday_price == before_yesterday_price:
        return "0 %"
    try:
        return str(round((abs(yesterday_price - before_yesterday_price) / before_yesterday_price) * 100.0, 2)) + " %"
    except ZeroDivisionError:
        return "0 %"

print(compare_close_price())

if compare_close_price() > "5":
    articles_list = [news_data["articles"][index]["title"] for index in range(0, 3)]
    print(articles_list)
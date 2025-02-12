import requests
import openai
from transformers import pipeline

# Sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis', model='finiteautomata/bertweet-base-sentiment-analysis')

def get_investment_advice(sentiment_score, stock_data):
    prompt = f"Given the sentiment score of {sentiment_score}, derived from a relevant news headline and article that provides insight into public perception, how might this influence stock prices? Along with the provided stock data {stock_data}, what would your investment recommendation be? Where should I invest?"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a financial advisor."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content


def get_stock_data(symbol):
    api_key = ('FINNHUB_API_KEY')
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    response = requests.get(url)
    return response.json()
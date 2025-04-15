import requests
import openai
from transformers import pipeline

# Sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis', model='finiteautomata/bertweet-base-sentiment-analysis')

def get_investment_advice(sentiment_score, stock_data, sector):
    prompt = (
    f"Given the overall sentiment score of {sentiment_score} from news articles, and stock name and data {stock_data}, "
    f"considering that the company operates in the {sector} sector, "
    f"what is your investment recommendation? What should an investor consider?"
)

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
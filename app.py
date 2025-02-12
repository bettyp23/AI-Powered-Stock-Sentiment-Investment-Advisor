from flask import Flask, render_template, request
import openai
from stock_sentiment import get_investment_advice, get_stock_data

from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Route to the homepage with the input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to get investment advice based on user input
@app.route('/advice', methods=['POST'])
def get_advice():
    sentiment_score = request.form['sentiment_score']
    stock_data = request.form['stock_data']
    
    # Fetch investment advice
    advice = get_investment_advice(sentiment_score, stock_data)
    
    return render_template('advice.html', advice=advice)

if __name__ == '__main__':
    app.run(debug=True)
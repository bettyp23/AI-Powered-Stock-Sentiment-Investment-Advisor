# AI-Powered Stock Sentiment Investment Advisor

This web application provides investment recommendations based on stock sentiment analysis. It uses AI to analyze the sentiment of news or other textual data related to a specific stock, and combines this with real-time stock price data to provide investment advice.

## Features

- **AI-Powered Sentiment Analysis**: The app analyzes sentiment based on a given sentiment score to determine whether a stock is trending positively or negatively.
- **Investment Advice**: Based on the sentiment score and recent stock data, the app provides investment recommendations such as whether to buy, hold, or sell a stock.
- **User-Friendly Interface**: The application presents the recommendation in a clean, easy-to-understand interface, designed for non-technical users.
- **Responsive Design**: The app adjusts to different screen sizes for optimal viewing on mobile, tablet, or desktop devices.

## Tech Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript (for dynamic content)
- **AI API**: OpenAI API for sentiment analysis
- **Stock Data**: Integrating with stock market APIs for real-time stock data

## Setup

### Prerequisites

- Python 3.x
- Flask
- OpenAI Python client
- A stock market data provider API key (e.g., Alpha Vantage, Yahoo Finance, or similar)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/AI-Powered-Stock-Sentiment-Investment-Advisor.git
    cd AI-Powered-Stock-Sentiment-Investment-Advisor
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for API keys:
    - Add your OpenAI API key
    - Add your stock market data API key

4. Run the application:
    ```bash
    python app.py
    ```

5. Access the application by visiting `http://localhost:5000` in your web browser.

## Files and Structure

- **`app.py`**: The main Flask application, which handles the backend logic and routes.
- **`templates/advice.html`**: The HTML template for displaying investment advice to users.
- **`static/styles.css`**: The CSS file for styling the HTML template.
- **`stock_sentiment.py`**: The Python file for handling sentiment analysis and stock data processing.

## How It Works

1. **Sentiment Analysis**: The app uses an AI model to analyze the sentiment score of news or other text data related to a specific stock.
2. **Stock Data**: Real-time stock price data is fetched using a stock market API.
3. **Investment Recommendation**: The app calculates whether the sentiment is positive or negative, compares it with the stock’s recent performance, and provides an investment recommendation (buy, hold, sell).

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request. Here are some areas you can help with:
- Adding more features (e.g., multiple stock support, portfolio management)
- Improving sentiment analysis accuracy
- Enhancing the frontend design

## Acknowledgments

- OpenAI for providing the sentiment analysis API.
- Stock data API providers for real-time stock information.
- Flask for making it easy to create web applications.
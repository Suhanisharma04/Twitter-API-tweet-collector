# Twitter API Tweet Collector

This project collects and saves the latest tweets from the official **@CommBank** Twitter account using the **Twitter API v2** and Python. It is a starting point for analyzing customer interactions, support trends, and sentiment on social media.

## Project Goals

- Connect to the Twitter API using Python
- Fetch the most recent 100 tweets from @CommBank
- Export the tweet data (text, author ID, timestamps) to a CSV file
- Lay groundwork for sentiment analysis and customer feedback insights

## Tools & Technologies

- Python 3.x
- Twitter API v2
- `requests`
- `pandas`

## Install required packages:
pip install -r requirements.txt

## Add your Twitter API credentials in a file called config.py:
- API_KEY = "your_api_key"
- API_KEY_SECRET = "your_api_secret"
- BEARER_TOKEN = "your_bearer_token"

# Run the script

# Output:
A CSV file named commbank_recent_tweets.csv will be created with tweet data

## Output Fields
- text – Tweet content
- created_at – Timestamp of the tweet
- author_id – ID of the user who posted it
- id – Tweet ID
## Future Additions
- Sentiment analysis using TextBlob or VADER
- Topic classification for customer issues
- Streamlit dashboard or Tableau visualizations
- Comparison with competitor bank Twitter activity







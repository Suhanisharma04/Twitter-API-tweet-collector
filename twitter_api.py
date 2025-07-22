import requests
import pandas as pd


API_KEY = "your_api_key_here"
API_KEY_SECRET = "your_api_secret_key_here"
BEARER_TOKEN = "your_bearer_token_here"
headers= {"Authorization": f"Bearer {BEARER_TOKEN}"}

handle = "CommBank"

url = (
    f"https://api.twitter.com/2/tweets/search/recent"
    f"?query=from:{handle}"
    f"&max_results=100"
    f"&tweet.fields=created_at,text,author_id"
    f"&expansions=author_id"
    f"&user.fields=username")



response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    tweets = data.get("data", [])

    if tweets:
        df = pd.DataFrame(tweets)
        print(df.head())
        df.to_csv("commbank_recent_tweets.csv", index = False)
        print("Tweets saved to 'commbank_recent_tweets.csv'")
    else:
        print("No tweets found.")
else:
    print(f"Failed to fetch tweets. Status code: {response.status_code}")
    print(response.text)



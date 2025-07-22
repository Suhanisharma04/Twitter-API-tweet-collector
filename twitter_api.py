import requests
import pandas as pd


API_KEY = "wjTuiyD7dLswV7YHt15mJu3w3"
API_KEY_SECRET = "0wHvYOEoDkqmyagAXDkTnubDn7Ihdmm2FMjsOgxYFqGGm4OK9n"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABSk3AEAAAAARtLbgAknbcq%2FV7eef%2Bw%2B9fKWluE%3DKMeiPnVeRzFrsDNZs3gdAkuQIXsdUD3aF8H9IFqR06O1yzBtuN"

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



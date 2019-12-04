import tweepy

PUBLIC_API_KEY = 'zEAvFiqQI8HhhemPO3aFyNzT2'
SECRET_API_KEY = 'RFXB7VbbOzNs1nHo1BAEvuZArieqWVzgXtnBwz3lMJob4qraJk'

ACCESS_TOKEN_PUBLIC = '1201977948129021953-jlloxSB1fUD6cUCa4ZH0xscsEctw5t'
ACCESS_TOKEN_SECRET = 'bRGDNb5jq3BU17k9Y4ASP3TcuayhK4Ca4C5xD0A8DoakH'

#Setup authentication
auth = tweepy.OAuthHandler(PUBLIC_API_KEY, SECRET_API_KEY)
auth.set_access_token(ACCESS_TOKEN_PUBLIC, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
import tweepy

PUBLIC_API_KEY = 'zEAvFiqQI8HhhemPO3aFyNzT2'
SECRET_API_KEY = 'RFXB7VbbOzNs1nHo1BAEvuZArieqWVzgXtnBwz3lMJob4qraJk'

ACCESS_TOKEN_PUBLIC = '1201977948129021953-jlloxSB1fUD6cUCa4ZH0xscsEctw5t'
ACCESS_TOKEN_SECRET = 'bRGDNb5jq3BU17k9Y4ASP3TcuayhK4Ca4C5xD0A8DoakH'

LIST_NAME = 'Users-Following'

#Setup authentication
auth = tweepy.OAuthHandler(PUBLIC_API_KEY, SECRET_API_KEY)
auth.set_access_token(ACCESS_TOKEN_PUBLIC, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


#Create the list the users will be added to
our_list = api.create_list(LIST_NAME, mode='private', description='List of users I was following')

#print(vars(our_list))

#print(our_list.id)

for friend_id in api.friends_ids():
    #print(friend_id)
    api.add_list_member(list_id=our_list.id, user_id=friend_id, owner_id=api.me().id)
#    print(api.get_user(friend_id), "\n \n")
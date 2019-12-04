import tweepy

PUBLIC_API_KEY = 'zEAvFiqQI8HhhemPO3aFyNzT2'
SECRET_API_KEY = 'RFXB7VbbOzNs1nHo1BAEvuZArieqWVzgXtnBwz3lMJob4qraJk'

ACCESS_TOKEN_PUBLIC = '1201977948129021953-rXYtx0sRPCirC38khhTq75U6eLyTJN'
ACCESS_TOKEN_SECRET = '7RolN6uSrgdzltnQEylMfYK6NAAWJHvejPsaELyXG7ll9'

LIST_NAME = 'Users-Following'
LIST_PRIVATE = True     #Set to False if you want the list public
LIST_DESCRIPTION = 'List of users I was following'

print('Running Twitter Following to List Migration Script...\n')

#Setup authentication
auth = tweepy.OAuthHandler(PUBLIC_API_KEY, SECRET_API_KEY)
auth.set_access_token(ACCESS_TOKEN_PUBLIC, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#Set list mode to correct value
list_mode = 'private' if LIST_PRIVATE else 'public'

#if list already exists add to it, otherwise create new list
list_already_exists = False
for current_list in api.lists_all():
    if current_list.name == LIST_NAME:
        our_list = current_list
        list_already_exists = True

#Create new list if it doesn't exist already
if not list_already_exists:
    our_list = api.create_list(LIST_NAME, mode=list_mode, description=LIST_DESCRIPTION)

#Iterate through friends adding them to list then unfollowing them
for friend_id in api.friends_ids():
    api.add_list_member(list_id=our_list.id, user_id=friend_id, owner_id=api.me().id)
    api.destroy_friendship(friend_id)

print('Script has finished running.')
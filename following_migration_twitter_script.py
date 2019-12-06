import tweepy

PUBLIC_API_KEY = 'rmX8xp2bw9YQujntaIJZjCPVN'
SECRET_API_KEY = 'hjbzXudPrBHr8wkhpZm3LRPGYcSU5bQjuxyvNhwKLTxct3QN26'

ACCESS_TOKEN_PUBLIC = '1201977948129021953-xnRqYL8OrTga3x6J0GKsRDaAvhFPbx'
ACCESS_TOKEN_SECRET = 'HlKNMoupQDR2rxMobzFKbiyiHxgV8tbEF68eMG7zM1u5X'

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

#Get total count of those we are following
following_count = len(api.friends_ids())

num_added_to_list = 0
#Iterate through friends adding them to list
for friend_id in api.friends_ids():
    api.add_list_member(list_id=our_list.id, user_id=friend_id, owner_id=api.me().id)
    num_added_to_list += 1

#Verify that every person we're following is added to list
if num_added_to_list == following_count:
    verified = True
else:
    verified = False

if verified:
    #Iterate through friends unfollowing them
    for friend_id in api.friends_ids():
        api.destroy_friendship(friend_id)
    print('Script has finished running successfully.')
else:
    print("ERROR - Not all follows were added to list, not unfollowing users.")
    print('Script has been terminated due to error.')

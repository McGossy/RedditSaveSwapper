
import json
from Accounts import SavedPostsSourceAccount, SavedPostsRecieverAccount

'''This project is dedicated to transfering Saved reddit submissions from one account to another.
    Note: This only works for saved submissions, not comments'''

file = open('reddit_info.json')
info = json.load(file)

accounts = []
accounts.append(info[0]['username'])
accounts.append(info[1]['username'])

post_limit = 10 #Change to integer to limit your post_limit(reduces time by a ton)

#testing taking curated saves from source account and saving them to reciever account
source_account = SavedPostsSourceAccount(accounts[0], post_limit=post_limit)
source_saves = source_account.get_pref_saved_posts(og_order=False, subreddits=['minecraft', 'blender'])

print('\n|||All filtered saves gathered|||')
for post in source_saves:
    print('Title:', post.title)
    print('Subreddit:', post.subreddit, '\n')

print('\n||Beginning Transfer||')
reciever_account = SavedPostsRecieverAccount(accounts[1], add_saves=source_saves, post_limit=post_limit)
reciever_account.save_pref_posts()

#This will remove the transfered saves from the source account.
#Do not use this unless you want to complete the transfer
#source_account.remove_pref_posts()

print('\n\n|Transfer Complete|\n\n')


#This section is dedicated to testing out the GET method for saved posts
og = SavedPostsSourceAccount(accounts[0], post_limit=post_limit) #sets up class

#get_pref_saved_post test cases (Only uncomment one of these lines at a time)
new_saved = []
#new_saved = og.get_pref_saved_posts() #gets ALL saved posts (up to specified limit)
#new_saved = og.get_pref_saved_posts(nsfw=True) #pulls all NSFW posts
#new_saved = og.get_pref_saved_posts(subreddits=['minecraft', 'videos', 'blender']) #pulls only from those subreddits
#new_saved = og.get_pref_saved_posts(omit_subs=['minecraft', 'videos', 'blender']) #omits these subreddits
#new_saved = og.get_pref_saved_posts(nsfw=True, subreddits=['videos', 'blender']) #pulls only NSFW content from these subreddits
#new_saved = og.get_pref_saved_posts(nsfw=True, omit_subs=['nsfw', 'horror']) #omits and only gets NSFW

if len(new_saved) > 0:
    print('|Printing saved posts after filters|')

for post in new_saved:
    print('Title:', post.title)
    print('Subreddit:', post.subreddit, '\n')
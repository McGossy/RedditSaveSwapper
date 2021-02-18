# RedditSaveSwapper
Takes two reddit accounts and swaps saves from one to the other. 
The goal of this project is to aid users who have too many saved posts from too many places. This project is meant to be used as a filtration system for these types of users. You can now have all your work/motivation related saves on one account and your fun saves on another.


# How to use:
To use this program you will need two seperate reddit accounts, both with access to the reddit API

Once that requirement is met you will need to update the 'reddit_info.json' file with your account & API information.

You will probablly also need to install praw which is reddits API python package. pip install praw

The rest is up to the user at the moment. There are no user prompts but the code is well documented. Make any changes you see fit and have fun!



# Future additions:
-GUI interface with plenty of user prompts.
-Ability to maintain just one account instead of requiring two to use.
-Sorting saved posts by subreddit for either account
-Ability to sort saved comments as well as submissions
-Possibly changing classes to use inheritance, since they share a lot of the same aspects
-Possibly create a mock-up reddit page that allows for live sorting without changing your save structure : Long shot, no clue how to achieve this

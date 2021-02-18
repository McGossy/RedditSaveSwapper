import praw
import json

file = open('reddit_info.json')
info = json.load(file)

#sets up reddit objects
def reddit(user_num):
    reddit = praw.Reddit(client_id = info[user_num]['client_id'],
                        client_secret = info[user_num]['client_secret'],
                        user_agent = info[user_num]['user_agent'],
                        username = info[user_num]['username'],
                        password = info[user_num]['password'])
    return reddit

#Sets up source account saves
class SavedPostsSourceAccount():
    def __init__(self, accountName, post_limit=50):
        self.source_redditor = reddit(0).redditor(accountName).saved(limit=post_limit)
        self.source_reddit = reddit(0)  # change later
        self.saved_posts = []
        self.get_all_saved_posts()

    #initializes all saved posts up to the specified limit
    def get_all_saved_posts(self):
        for saved in self.source_redditor:
            if isinstance(saved, praw.models.Submission):
                self.saved_posts.append(saved)
        return self.saved_posts

    #get the saved posts you wish to transfer based on some variables
    #og_order determines the order you will see your saves pop up on your saved page, True=original, False=Reversed
    #nsfw determines you want to gather NSFW posts or not
    #subreddits is a list of subreddits you want to filter for transfer : use strings
    #omit_subs is a list that filters the subreddits you do not wish to transfer : use strings
    def get_pref_saved_posts(self, og_order=True, nsfw=False, subreddits=[], omit_subs=[]):

        #preserves order if True
        if og_order == True:
            reversed_posts = []
            for i in reversed(self.saved_posts):
                reversed_posts.append(i)
            self.saved_posts = reversed_posts

        #curates posts based on preferences
        curated_posts = []
        for saved in self.saved_posts:
            # if no subreddits listed, continue branch
            if not subreddits:
                # finds all post except those omitted
                if nsfw == False:
                    if saved.subreddit not in omit_subs:
                        curated_posts.append(saved)
                # finds all NSFW posts except those ommited
                else:
                    if saved.subreddit not in omit_subs and saved.over_18:
                        curated_posts.append(saved)
            # for specific subreddits. no need for omit_subs in this branch
            else:
                # finds posts only from specific subreddits
                if nsfw == False:
                    if saved.subreddit in subreddits:
                        curated_posts.append(saved)
                # finds posts only from specifc subreddits & they must be nsfw marked
                else:
                    if saved.subreddit in subreddits and saved.over_18:
                        curated_posts.append(saved)

        self.saved_posts = curated_posts

        return self.saved_posts

    # will sort saved_posts by subreddits in order // fill in later
    def sort_pref_posts_subreddit(self, subreddits):
        for saved in self.saved_posts:
            print('', sep='', end='')

    # removes/unsaves all posts listed in self.saved_posts : if you wish to remove after a transfer
    def remove_pref_posts(self):
        for saved in self.saved_posts:
            submission = self.source_reddit.submission(id=saved)
            submission.unsave()

    # resaves all posts listed in self.saved_posts, bringing all preferred posts to the top
    def save_pref_posts(self):
        for saved in self.saved_posts:
            submission = self.source_reddit.submission(id=saved)
            submission.save()

#Sets up Reciever account for saves to be transferred to
class SavedPostsRecieverAccount():
    def __init__(self, accountName, add_saves, post_limit=50):
        self.reciever_redditor = reddit(1).redditor(accountName).saved(limit=post_limit)
        self.reciever_reddit = reddit(1)  # change later
        self.pref_saved = add_saves
        self.all_saved = []
        self.get_all_saved_posts()

    def get_all_saved_posts(self):
        for saved in self.reciever_redditor:
            if isinstance(saved, praw.models.Submission):
                self.all_saved.append(saved)
        return self.all_saved

    # will sort pref_saved by subreddits in order
    def sort_pref_posts_subreddit(self, subreddits):
        for saved in self.pref_saved:
            print('', sep='', end='')

    # this one kinda just belongs in the SavedPostsSourceAccount class
    # removes/unsaves all posts listed in self.pref_saved
    def remove_pref_posts(self):
        for saved in self.pref_saved:
            submission = self.reciever_reddit.submission(id=saved)
            submission.unsave()

    # resaves all posts listed in self.pref_saved, bringing all preferred posts to the top
    def save_pref_posts(self):
        for saved in self.pref_saved:
            submission = self.reciever_reddit.submission(id=saved)
            submission.save()

    # removes all saved posts. Starts in blank state
    def remove_all_saved_posts(self):
        print('in remove all posts')
        for saved in self.all_saved:
            submission = self.reciever_reddit.submission(id=saved)
            submission.unsave()

# Alexander Dietz
# Brittani Kiger
# Christopher Lytle

# Import praw
import praw

# Import local config file
import config

# Import login credentials

def login():
    obj = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret)
    return obj

def bot(obj):
    for comment in login.subreddit('test').comments(limit=25):
        if "python" in comment.body:
            print("String found!")

obj = login()
bot(obj)
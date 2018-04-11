# Alexander Dietz
# Brittani Kiger
# Christopher Lytle

# Import praw
import praw

# Import local config file
import config

# Import login credentials
import credentials

def login():
    obj = praw.Reddit(username = credentials.username,
                password = credentials.password,
                client_id = credentials.client_id,
                client_secret = credentials.client_secret)
    return obj

def bot(obj):
    for comment in obj.subreddit('test').comments(limit=25):
        if "python" in comment.body:
            print("String found!")

obj = login()
bot(obj)
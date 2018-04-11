# Alexander Dietz
# Brittani Kiger
# Christopher Lytle

# Import praw
import praw

# Import local config file
import config

# Import login credentials
import credentials

# Function to log bot into reddit
def login():
    obj = praw.Reddit(username = credentials.username,
                password = credentials.password,
                client_id = credentials.client_id,
                client_secret = credentials.client_secret,
                user_agent = "CalU Python bot test v0.1")
    return obj

# Function that searches for string within comments on /r/test
def bot(obj):
    for comment in obj.subreddit('test').comments(limit=25):
        if "test" in comment.body:
            print("String found!")

# Creates login object
obj = login()

# Runs bot using login object
bot(obj)
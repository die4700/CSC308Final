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
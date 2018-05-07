import praw
import config
import time
import os
import re
import scraper

scraper.run_scraper()
scraper.removeWebTags()

def bot_login():
    print ("Logging in...")
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "basedcraft's test bot comment responder")
                
    print ("Logged in!")

    return reddit

def run_bot(reddit, comments_replied_to):
    print ("Obtaining 10 comments..." )

    for submission in reddit.subreddit('test').new(limit=20):
        if submission.id not in comments_replied_to and submission.author != r.user.me():
            if re.search("Community Update", submission.title, re.IGNORECASE):
                print("Title: " + submission.title)
                print("String with \"Community Update\" found! " + submission.id)

                with open('balanceChanges.txt', 'r') as readFile:
                    data = readFile.read()

                submission.reply(data)
                print("Replied to comment " + submission.id)

                with open("comments_replied_to.txt", "a") as f:
                    comments_replied_to.append(submission.id)
                    f.write(submission.id + "\n")


#sleep for 10 seconds
    print ("Sleeping for 10 seconds...")
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    
    else:
        with open ("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()

while True:
    run_bot(r, comments_replied_to)



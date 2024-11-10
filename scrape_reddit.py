import praw
from collections import defaultdict

def create_reddit_access():
    return praw.Reddit(
        client_id='CLIENT_ID',
        client_secret='CLIENT_SECRET',
        user_agent='USER_AGENT'
    )

def create_subreddit_access(reddit, subreddit_name):
    return  reddit.subreddit(subreddit_name)

def add_post_comments(submission, results):
    """
    Adds the posts and comments from the specified submission
    to the results list.
    """
    results.append({
            "author": submission.author,
            "text": submission.selftext
        })

    submission.comments.replace_more(limit=0)  # Flatten comment tree
    for comment in submission.comments.list():
        results.append({
            "author": comment.author,
            "text": comment.body
        })

def scrape_subreddit(subreddit_name):
    """
    Scraped posts and comments from the specified subreddit.
    Returns a list of "posts". Each post is a dictionary with
    that post/comment's author and text.
    """

    reddit = create_reddit_access()

    subreddit = create_subreddit_access(reddit,  subreddit_name)

    # List to hold all the scraped posts and comments 
    results = []
    post_limit = 50

    for submission in subreddit.new(limit=post_limit):
        add_post_comments(submission, results)
               
    return results

def print_results(results):
    for post in results:
        print(f"Post author: {post['author']}")
        print(f"Text: {post['text']}")
        print("\n" + "-"*40 + "\n")


from textblob import TextBlob
from scrape_reddit import scrape_subreddit

interest_keywords = ['clinical trial', 'study', 'research', 'participate', 'experiment', 'new treatments', 'innovative treatments', 'alternative treatment']
benefit_keywords = ['severe symptoms', 'no improvement', 'getting worse', 'advanced stage', 'late stage', 'persistent symptoms']

def analyze_text_sentiment(text):
    """
    Returns the polarity of the text's sentiment
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity 

def contains_keyword(text, keywords):
    """
    Returns true if any of the words in the keywords list are in the 
    specified text.
    """
    text = text.lower()

    for word in keywords:
        if word in text:
            return True
    
    return False

def analyze_interestlevel(results):
    """
    Adds the 'sentiment' and 'interest level' field to all the
    posts in the results list.
    """
    for post in results:
        post['sentiment'] = analyze_text_sentiment(post['text'])
        classify_user(post)

def classify_user(post):
    """
    Adds the 'interest level' to the specified post.
    Classifies the post as Interested, Could Benefit or Not Interested/Irrelevant 
    based on sentiment and keywords.
    """
    if contains_keyword(post['text'], interest_keywords) and post['sentiment'] > 0.0:
        post['interest level'] = 'Interested'
    elif contains_keyword(post['text'], benefit_keywords) and post['sentiment'] <= 0.0:
        post['interest level'] = 'Could Benefit'
    else:
        post['interest level'] = 'Not Interested/Irrelevant'
       

import openai
from scrape_reddit import scrape_subreddit
from segement_interestlevel import analyze_sentiment

condition = "ovarian cancer"

openai.api_key = 'OPENAI_KEY'

def generate_message(post):
    """
    Generates a message based on the post's interest level and text to engauge
    the user about clinical trails. Only generates a message for 'Interested'
    and 'Could Benefit' interest levels.
    """
    
    if post['interest level'] == 'Interested':
        prompt = f"Write a message to enguage someone interested in participating in a clinical trial for {condition}. Include benefits and clear next steps. They mentioned {post['text']}"
    elif post['interest level'] == 'Could Benefit':
        prompt = f"Write an informative message for someone who may benefit from clinical trials for {condition} but might not know about them. Explain clinical trials and the potential benefits. They mentioned {post['text']}"
    else:
        return None
    
    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
        
   
    return response.choices[0].message.content


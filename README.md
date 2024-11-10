# Tumerik_ML
Setup:

    Required Packages
    Make sure you have the following packages installed:

    textblob: For text processing and sentiment analysis.
    openai: To interact with the OpenAI API.
    praw: For accessing and scraping data from Reddit.

    To install these packages, use:
    pip install textblob openai praw

    Python Version
    This project is designed to run on Python 3.10.2. Ensure your environment is set to this version or compatible with it.

    Configuration
    1. Reddit Access:
    - Open the scrape_reddit.py file.
    - Fill in CLIENT_ID, CLIENT_SECRET, and USER_AGENT with your Reddit API credentials.
    - For information on setting up Reddit API credentials, refer to the PRAW Quickstart Guide.

    2. OpenAI API Access:
    - Open the generate_messages.py file.
    - Set your OpenAI API key by filling in the OPENAI_KEY variable with your API key.

    3. Search Condition:
    - This version of the project is currently set up to gather data related to ovarian cancer and will search the ovariancancer subreddit.
    - To change the condition, update the SUBREDDIT_NAME variable in main.py with your desired subreddit.
    - Update the condition variable in generate_messages.py to reflect the new topic or condition you wish to target.

Running the Project:

    To start the project, use:

    python main.py

Methodology / Challenges:
    Method

    1. Reddit Data Scraping:
    - Scrape a predetermined relevant subreddit for the newst posts.
    - Gather the author and text of the post and comments for further analysis.
    
    2. Sentiment Analysis:
    - Using TextBlob, analyze the polarity of sentiment of the text in each post and comment. Allows assessing whether the content has a positive, neutral, or negative sentiment.
    
    3. Segmenting Posts by Interest:
    - Based on the text content and sentiment, classify each post as one of the following:
        - Interested: Posts that contain an interest-related keyword (e.g., "clinical trial", "research") and have a positive sentiment.
        - Could Benefit: Posts that contain a benefit-related keyword (e.g., "severe symptoms", "no improvement") and have a negative or neutral sentiment.
        - Not Interested/Irrelevant: Posts that do not meet the criteria for either "Interested" or "Could Benefit."
    
    - Keywords:
        Interest-related keywords: {'clinical trial', 'study', 'research', 'participate', 'experiment', 'new treatments', 'innovative treatments', 'alternative'}
        Benefit-related keywords: {'severe symptoms', 'no improvement', 'getting worse', 'advanced stage', 'persistent symptoms', 'any recommendations', 'help', 'advice'}
    
    4. Message Generation:
    - For posts classified as Interested or Could Benefit, a tailored message is generated using the OpenAI API. Different prompts are used for each category, and the post's text is incorporated into the prompt to create a personalized response.
   
    Challenges / Potential Improvements
   
    1. Aggregating User Data:
    - Aggregating all the posts and comments made by a single user could provide more context about each user and improve classification accuracy and message generated.

    2. Machine Learning for Classification:

    - Implementing a machine learning model could help improve the classification of posts as "Interested", "Could Benefit", "Not Interested/Irrelevant"
    - This model could also assist in finding better keywords and adjusting the sentiment thresholds for classification.
    
    3. Keyword Count vs. Presence:
    - Currently, just whether post contain specific keywords is considered. However, it may be more effective to consider the count of keywords found within a post. More keyword matches could indicate greater relevance to the target condition.
    
    4. Named Entity Recognition (NER):
    - NER techniques could be applied to extract entities such as symptoms, previous treatments, and other medical details. 
    - This could be used to help further personalize the generated message or classify users based on the specifics of their posts.
    
    5. Expanding Subreddit Coverage:

    - The project currently looks at a single subreddit (ovariancancer). Expanding the search to include more subreddits and/or broader subreddits could increase the reach of responses. 
    - Filtering would be necessary to ensure that the posts are relevant to the condition of interest.
    
    6. Processing Comments:
    - Currently, posts and comments are treated independently.
    - It might be more effective to consider comment sentiment and comment content when classifying and generating messages for a post. 

Examples:


-------------------------------Text----------------------------------


I don't want to scare you with my story, only telling you because you need to always advocate for yourself and trust yourself.

Last March, I had imaging that showed small cysts that were characterized as benign and told they are common and come and go.  I had my well-woman exam in May - all was fine.

I've also had IBS and other digestive issues for decades; so, I pretty much brush off bowel changes and abdominal discomfort/pain as my normal.

Then at the end of August,  I can't breathe well and am admitted to the hospital. Long story short,  diagnosed with Stage IV ovarian cancer that has metastasis outside the abdomen (to lung pleura).

Fine in May; Advanced cancer by August.

Ovarian cancer is quick and very hard to detect early.  There's no screening for ovarian cancer as far as I have read, like mammogram is for breast cancer. I know cancer research centers are working on it.

Advocate for yourself always.   Personally,  I wouldn't wait 10 to 12 weeks for followup. Screw that. They can do blood workup and biopsy, if viable.      

--------------------------Interest Level-----------------------------

Interested

-----------------------------Response--------------------------------

Hello,

Thank you for sharing your story and for advocating for yourself. It's important to be proactive when it comes to your health, especially when it comes to conditions like ovarian cancer.

If you're interested in participating in a clinical trial for ovarian cancer, there are many benefits. Clinical trials give you access to cutting-edge treatments and therapies that may not be available through standard care. You'll also be contributing to the advancement of medical knowledge and helping others who may be facing similar challenges.

The next steps would be to talk to your healthcare provider about potential clinical trials in your area. They can provide you with information on eligibility criteria and help guide you through the process of participating in a trial. You can also research clinical trials online and reach out to research centers directly.

Remember, advocating for yourself and trusting your instincts are key. Don't hesitate to seek out additional options and resources in your journey.        

Take care and all the best on your path to healing.

Sincerely, [Your Name]


-------------------------------Text----------------------------------

Hi everyone ❤️ I'm 32f

Back in Feb of this year I got my period back after having my second kiddo. My periods have always been wonky but I've been on bc for well over a decade. Well, this summer period pains and ovulation pain got worse, ended up with a complex cyst on both ovaries, which both burts one month after the other. GYN wasn't too concerned.

Fast forward, pain has gotten worse, suspecting endo. Have lap scheduled for Dec. However, in the last month, my symptoms have increased yet again to the following: ovary pain(heavy on my left side) is almost constant, full abdominal cramping, bloating, loss of appetite(I'm also on Vyvanse but quit taking it to make sure I truly wasn't hungry), feeling full quick, changes to bowel habits(used to be beautifully regular) and insane fatigue.

I'm worried that with this progression we may be dealing with more than just endo, i.e. ovarian cancer since that's where the majority of my sharp pains/aches are. I'll also note that I put my raw DNA through promethease and it hit for 2 BRCA1 mutations amongst other markers, and my maternal aunt passed from stage 4 ovarian cancer. I'm also scheduled in Nov to see a genetic counselor for those markers.

With all this in mind, should I bring it up to my pcp about my worsening symptoms? I've had so many appointments recently and another tvus a month a go that came back clear. Is it just endo that's getting worse or something more serious?
--------------------------Interest Level-----------------------------

Could Benefit

-----------------------------Response--------------------------------

Hi there! It sounds like you are going through a lot and I'm sorry to hear that you are experiencing such concerning symptoms. Given your family history of ovarian cancer and the genetic markers that you have, it's completely understandable that you are feeling anxious about the possibility of having a more serious condition.

I wanted to let you know about the option of participating in clinical trials for ovarian cancer. Clinical trials are research studies that test new treatments or interventions for a variety of medical conditions, including ovarian cancer. By participating in a clinical trial, you would have access to cutting-edge treatments that are not yet available to the general public. This could potentially offer you new options in managing your symptoms and improving your quality of life.

Additionally, participating in a clinical trial can contribute to advancements in the field of ovarian cancer research, ultimately leading to better treatment options for future patients. It's a way to play an active role in your own healthcare and potentially benefit not only yourself but also others who may be facing similar challenges.

I would recommend discussing the possibility of clinical trials with your healthcare provider, as they may be able to provide you with more information and help you determine if it could be a beneficial option for you. It's important to weigh all of your treatment options and make an informed decision that aligns with your personal health goals.

I hope this information is helpful to you and that you find the support and care that you need during this difficult time. Take care of yourself and don't hesitate to reach out for more information or guidance. Stay strong and know that there are resources available to support you in your journey towards better health. ❤️


Ethical Considerations:
- No user data is stored in a permant database. Data is only processed temporarily for the analysis and message generation, with no long-term retention.
- The project does not explicitly extract or store any personal information (full name, address, date of birth, etc) of Reddit users. Only the text of posts and comments and the reddit username is accessed.
- As a potential future improvement, the project could be modified to extract only the relevant information from each post (ex. keywords or summaries) rather than including the entire post text in the prompt to the OpenAI API. This would minimize the data shared with the API while still personalizing message generation.

from scrape_reddit import scrape_subreddit
from segement_interestlevel import analyze_interestlevel
from generate_messages import generate_message

SUBREDDIT_NAME = "ovariancancer"

def main():
    results = scrape_subreddit(SUBREDDIT_NAME)
    analyze_interestlevel(results)

    for post in results:
        
        if post['interest level'] != 'Not Interested/Irrelevant':
            post['generated_message'] = generate_message(post)
            
            print("-------------------------------Text----------------------------------")
            print(post['text'])
            print("--------------------------Interest Level-----------------------------")
            print(post['interest level'])
            print("-----------------------------Response--------------------------------")
            print(post['generated_message'])
            print("\n")

if __name__ == "__main__":
    main()
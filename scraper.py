import requests
from bs4 import BeautifulSoup

def get_cos(ancestor, selector):
    return ancestor.select_one(selector).text.strip()

# product_code = input("Podaj kod produktu: ")
product_code = "95319759"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
# print(url)
response = requests.get(url)
page_dom = BeautifulSoup(response.text, 'html.parser')
page_dom.prettify()

opinions = page_dom.select("div.js_product-review")
#print(type(page_dom))
#print(type(reviews))
#print(len(reviews))

for opinion in opinions:
    single_opinion = {
        "opinion_id": opinion["data-entry-id"],
        "author": opinion.select_one("span.user-post__author-name").text.strip(),
        "recommendation": opinion.select_one("span.user-post__author-recomendation > em").text.strip(),
        "stars": opinion.select_one("span.user-post__score-count").text.strip(),
        "purchased": opinion.select_one("div.review-pz").text.strip(),
        "opinion_date": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchase_date": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].text.strip(),
        "useful": opinion.select_one("button.vote-yes")["data-total-vote"].strip(),
        "unuseful": opinion.select_one("button.vote-no")["data-total-vote"].strip(),
        "content": opinion.select_one("div.user-post__text").text.strip(),
        "cons": [cons.text.strip() for cons in opinion.select_one("div.review-feature__title--negatives ~ div.review-feature__item")],
        "pros": [pros.text.strip() for pros in opinion.select_one("div.review-feature__title--positives ~ div.review-feature__item")]

    }
    
all_opinions.append(single_opinion)
print(all_opinions)

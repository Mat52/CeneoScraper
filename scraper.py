import requests
from bs4 import BeautifulSoup

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
    print(opinion["data-entry-id"])

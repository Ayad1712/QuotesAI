import requests
from bs4 import BeautifulSoup
import random, time
url = "https://quotes.toscrape.com/"
quotes_url = requests.get(url)
#If the request is successful, it will return a status code of 200
parsed_quotes = BeautifulSoup(quotes_url.text, "html.parser")
#<span> is a tag name.
#class is an attribute for the <span> tag. It contains a value, in this case being "text"
#Tag name: span, Attribute: class, Value: text: all of the quotes have this exact attribute, tag, and value.
#In literal definition, the <span> is an html element that is used to group inline elements.
#In literal definition, the "text" value is an identifier to label that specific quote.
all_quotes = parsed_quotes.find_all("span", class_="text") #find_all is used to find all the elements with a specific tag, attribute, and value.
#now we need to use random to select a random quote 
random_item = random.choice(all_quotes)
random_quote = random_item.text #this will only print the text of the quote, not the tags or attrubutes.
question = input("What would you like me to do today? Ex: 'Give me a quote.': ")
if question == "Give me a quote.":
    print(f"Sure! A random quote for you: {random_quote}") #In normal ai's the quote scraping should be done when the question is asked, but for now it is done at the beginning.
#Challenge:
all_author_names = parsed_quotes.find_all("small",class_="author") 
author_seen = set()
for author in all_author_names:
    if author.text not in author_seen:
        print(author.text)
        author_seen.add(author.text)
        time.sleep(1)

import requests
from bs4 import BeautifulSoup

#1. USE REQUEST TO FETCH HTML
response =  requests.get("https://www.bbc.com/news")
print(response.status_code)

#2. USE BEAUTIPULSOUP TO PARSE H2 AND TITLE
soup = BeautifulSoup(response.text,'html.parser')
headlines = soup.find_all(['h3','h2'])

headlines_texts = []
for tag in headlines:
    text = tag.get_text(strip = True)
    if text and text not in headlines_texts:
        headlines_texts.append(text)

        #OR
# for tag in headlines:
#     text = tag.get_text(strip=True)
#     if text and len(text) > 10: # filters the short/empty lines
#         headlines_texts.append(text)

#3.  SAVING THE HEADINGS INTO A TXT FILE
with open("headlines.txt", "w") as file:
    for i, headline in enumerate(headlines_texts,1):
        print(f"{i}. {headline}")

print(f"{len(headlines_texts)} headlines saved to 'headlines.txt'")
        

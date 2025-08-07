# 📰 News Headlines Scraper

This Python script scrapes the latest news headlines from the [BBC News](https://www.bbc.com/news) homepage using `requests` and `BeautifulSoup`.

---

## 📌 Features

- Fetches the HTML content of BBC News homepage
- Parses and extracts all `<h2>` and `<h3>` tags (commonly used for headlines)
- Filters out duplicates and short/empty lines
- Saves the cleaned headlines into a `headlines.txt` file
- Prints the numbered headlines to the console

---

## 🛠️ Requirements

- Python 3
- `requests` library
- `beautifulsoup4` library

Install the dependencies with:

pip install requests 
pip install beautifulSoup4

📂 Output Example
1. Hurricane Idalia lashes Florida coast
2. Trump pleads not guilty to charges
3. India lands Chandrayaan-3 on the moon
...

👾 EXTRA
 for tag in headlines:
    text = tag.get_text(strip=True)
    if text and len(text) > 10: # filters the short/empty lines



<img width="1260" height="969" alt="Screenshot 2025-08-07 181412" src="https://github.com/user-attachments/assets/c6fa4b28-e016-47b0-ba22-c013d0995309" />



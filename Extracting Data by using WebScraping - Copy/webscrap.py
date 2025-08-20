import requests
from bs4 import BeautifulSoup
import pandas as pd

# base url of the best sellers page for teaching & education books
base_url = "https://www.amazon.in/gp/bestsellers/books/4149461031/ref=zg_bs_pg_{}?ie=UTF8&pg={}"

# http headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# initialize a list to store book data
book_list = []

# iterate over the first 3 pages to get top 50 books (assuming each page has about 20 items)
for page in range(1, 4):
    # construct the URL for the current page
    url = base_url.format(page, page)
    
    # send a GET request to the url
    response = requests.get(url, headers=headers)
    
    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")
    
    # find all the book elements
    books = soup.find_all("div", {"class": "zg-grid-general-faceout"})
    
    # iterate over each book element to extract data
    for book in books:
        if len(book_list) < 50:  # stop once we've collected 50 books
            author = book.find("a", class_="a-size-small a-link-child").get_text(strip=True) if book.find("a", class_="a-size-small a-link-child") else "N/A"
            rating = book.find("span", class_="a-icon-alt").get_text(strip=True) if book.find("span", class_="a-icon-alt") else "N/A"
            
            # append the extracted data to the book_list
            book_list.append({
                "Author": author,
                "Rating": rating
            })
        else:
            break


# convert the list of dictionaries into a DataFrame
df = pd.DataFrame(book_list)

print(df.head())

# save the DataFrame to a CSV file
df.to_csv("amazon_top_50_books_authors_ratings.csv", index=False)
import requests
from bs4 import BeautifulSoup



def scrape_marketnews_urls(url):
    # Open notepad file for writing
    file_write = open('news-urls.txt','w')
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all div tags that contain a ul tag
        div_tags = soup.find_all('div')

        # Iterate through the div tags and extract ul tags
        for div in div_tags:
            ul_tags = div.find_all('ul')
            
            # Filter and print ul tags without "menu" in their id
            for ul in ul_tags:
                ul_id = ul.get('id', '')
                if 'menu' not in ul_id.lower():
                    a_tags = ul.find_all('a')
                    for a in a_tags:
                        if a['href'] and 'http' in a['href']:
                            file_write.write(a['href'])
                            file_write.write("\n")


# Example usage
# url = 'https://biztoc.com/'  # Replace with the actual URL you want to scrape
# scrape_marketnews_urls(url)

def scrape_website_contents(url:str) -> str:
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract all the text from the body
        body_text = soup.body.get_text(separator='\n', strip=True)
        
        # Write the extracted text into a text file
        with open("url-content.txt", "w", encoding="utf-8") as file:
            file.write(body_text)
            
        print("Content successfully saved to url-content.txt")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

scrape_website_contents('https://finance.yahoo.com/news/palantir-stock-buy-high-091000665.html?ref=biztoc.com')

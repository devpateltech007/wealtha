from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
import asyncio
from requests.exceptions import Timeout, RequestException
from bs4 import BeautifulSoup

class scrapeProxyiumSelenium:
    def __init__(self, url: str, timeout: int = 5):

        proxyium_url = "https://cdn.proxyium.com/proxyrequest.php"
        payload = 'type=&url='+url
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'webproxy_ga=f16ec035-f1e3-4098-807e-652d40a322ed'
        }

        response = requests.request("POST", proxyium_url, headers=headers, data=payload, allow_redirects=False)

        # Print the response text
        print("Response content:")
        print(response.text)

        # Fetch and print the "Location" header
        location_header = response.headers.get('Location')
        print(location_header)

        # parsing the Proxyium API to reach final destination URL
        cpi_location = str(location_header).find('__cpi')
        r_location = str(location_header).find('&r=')

        r_string = location_header[r_location+3:]
        cpo_location = r_string.find("%")
        r_string = r_string[:cpo_location]
        print(r_string)
        cpo_string = r_string[:32]


        ip_string = location_header[:cpi_location]
        final_ip = ip_string + "world/uk/former-scottish-first-minister-alex-salmond-dies-at-69-99007c95" + "?__cpo=" + cpo_string
        # print(cpo_string)
        # follow_redirects(ip_string + "wiki/Kamala_Harris" + "?__cpo=" + cpo_string )

        # Setup Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
        # chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # Disable images
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--window-size=1920x1080")  # Set window size (optional)

        # Create WebDriver instance
        driver = webdriver.Chrome(chrome_options)
        print(final_ip)
        # Open a webpage
        driver.get(location_header)
        print("==",location_header)

        # Give the page some time to load (optional)
        time.sleep(timeout)

        if driver.find_element(By.XPATH, "//button[@name='agree' and @type='submit']"):
                agree_button = driver.find_element(By.XPATH, "//button[@name='agree' and @type='submit']")
                
                # Click the button
                agree_button.click()
                
                print("Button clicked successfully!")

        else:
             print("Accepting Cookies not needed")


        with open("url-content.txt", "w", encoding="utf-8") as file:
            page_source = driver.page_source
            soup = BeautifulSoup(page_source)
            print(soup.prettify)
            elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])  # Find all relevant tags
            print(str("\n".join(elem.get_text(strip=True) for elem in elements))) 
            file.write(str("\n".join(elem.get_text(strip=True) for elem in elements)))
        driver.quit()


scrapeProxyiumSelenium('https://finance.yahoo.com/news/palantir-stock-buy-high-091000665.html?ref=biztoc.com')
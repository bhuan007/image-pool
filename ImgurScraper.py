from bs4 import BeautifulSoup
from selenium import webdriver
import requests, os, time, math

# Modules for optimization on loads
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ImgurScraper():

# This is the Imgur Scraper class. The constructor requires two paramemters. 
# The first is searchTerm which is the category of images the user wants to search.
# The second is imgNum which is the number of images a user wants to download.

# The method scrape will initiate the webscraping application

    def __init__(self, searchTerm, imgNum):
        self.searchTerm = searchTerm
        self.imgNum = imgNum
        # This parameter will tell you how many images were NOT downloaded / FAILED
        self.errorCount = 0

    def scrape(self):
        # Create folder directory for images to be downloaded to
        os.makedirs('imgur', exist_ok=True)

        browser = webdriver.Chrome()
        browser2 = webdriver.Chrome()

        # Opening main search page and selecting all images...
        browser.get('https://imgur.com/search/score/all?q_type=jpg&q_all=' + self.searchTerm)

        # Number of scrolls needed to get required images
        scrollNum = math.floor(self.imgNum/60)

        # Scrolling the browser
        for i in range(scrollNum):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)

        #Adding image elements into an array
        imgArray = browser.find_elements_by_class_name('image-list-link')

        # Looping through image array and selecting each href to higher quality image
        for x in imgArray[:self.imgNum]:
            pictureAddress = x.get_attribute('href')
            
            try: 
                browser2.get(pictureAddress)
                # Waiting for the image to load first before moving on... timeout if load lasts longer than 3 seconds
                try:
                    elementLoaded = EC.presence_of_element_located((By.CLASS_NAME, 'image-placeholder'))
                    WebDriverWait(browser2, 3).until(elementLoaded)
                except TimeoutException:
                    self.errorCount += 1
                finally:
                    # Finding the image and downloading it to imgur folder
                    imgDiv = browser2.find_element_by_class_name('image-placeholder')
                    imgLink = imgDiv.get_attribute('src')
                    res = requests.get(imgLink)
                    imageFile = open(os.path.join('imgur', os.path.basename(imgLink)), 'wb')

                    for chunk in res.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()

                    #Finding image metadata adding it to a csv file
                    page = requests.get(pictureAddress)
                    soup = BeautifulSoup(page.text, 'html.parser')

                    title = soup.select_one('post-title')
                    print(title)

            except:
                continue

        browser.quit()
        browser2.quit()

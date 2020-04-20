from bs4 import BeautifulSoup
from selenium import webdriver
import requests, os, time, math, csv, datetime, re

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
        # Creating main imgur folder along with subfolder for a specific search
        timeFormat = datetime.datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
        subfolderName = f'{timeFormat}-{self.searchTerm}'
        os.makedirs(f'imgur/{subfolderName}', exist_ok=True)

        #Creating and writing header to csv file
        with open(f'imgur/{subfolderName}/{self.searchTerm}-meta.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'title', 'author', 'date', 'points', 'views', 'comments', 'version'])

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
                    # *****VERSION 2*****
                    try:
                        elementLoaded = EC.presence_of_element_located((By.XPATH, "//div[@class='image post-image']//img"))
                        WebDriverWait(browser2, 3).until(elementLoaded)
                    except TimeoutException:
                        self.errorCount += 1
                    else:
                        # Finding the image and downloading it to imgur folder
                        imgElement = browser2.find_element_by_xpath("//div[@class='image post-image']//img")
                        imgLink = imgElement.get_attribute('src')
                        res = requests.get(imgLink)
                        imgId = str(os.path.basename(imgLink))
                        imageFile = open(os.path.join(f'imgur/{subfolderName}', imgId), 'wb')

                        for chunk in res.iter_content(100000):
                            imageFile.write(chunk)
                        imageFile.close()

                        #Printing metadata
                        self.outputMeta(browser2, 2, imgId, subfolderName)

                else:
                    # *****VERSION 1*****
                    # Finding the image and downloading it to imgur folder
                    imgDiv = browser2.find_element_by_class_name('image-placeholder')
                    imgLink = imgDiv.get_attribute('src')
                    res = requests.get(imgLink)
                    imgId = str(os.path.basename(imgLink))
                    imageFile = open(os.path.join(f'imgur/{subfolderName}', imgId), 'wb')

                    for chunk in res.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()

                    #Printing metadata
                    self.outputMeta(browser2, 1, imgId, subfolderName)

            except:
                continue

        browser.quit()
        # while True:
        #     pass
        browser2.quit()

    def outputMeta(self, browser, version, id, subfolderName):
        if (version == 1):
            title = browser.find_element_by_xpath("//div[@class='Gallery-Title']/div/span").text
            try:
                author = browser.find_element_by_xpath("//a[@class='author-link']/span").get_attribute('title')
            except :
                author = 'N/A'
            views = browser.find_element_by_xpath("//div[@class='Meta']/span").text
            date = browser.find_element_by_xpath("//div[@class='Meta']/span[3]").get_attribute('title')
            comments = browser.find_element_by_xpath("//div[@class='CommentsList-headline--counter']/span").text
            points = browser.find_element_by_xpath("//span[@title='Total Score']").text
        
        elif (version == 2):
            title = browser.find_element_by_xpath("//h1[@class='post-title']").text
            try:
                author = browser.find_element_by_xpath("//a[@class='post-account']").text
                try:
                    date = browser.find_element_by_xpath("//div[@class='post-title-meta font-opensans-semibold']/span[3]").get_attribute('title')
                except:
                    date = browser.find_element_by_xpath("//div[@class='post-title-meta font-opensans-semibold']/span[2]").get_attribute('title')
            except:
                author = 'N/A'
                date = browser.find_element_by_xpath("//div[@class='post-title-meta font-opensans-semibold']/span").get_attribute('title')
            views = browser.find_element_by_xpath("//span[@class='post-action-stats pointer']/span[2]").text
            comments = browser.find_element_by_xpath("//span[@class='comments-count']").text
            points = browser.find_element_by_xpath("//span[@class='post-action-stats-points']").text
            
        
        idSliced = id[:-4]
        pointsRegex = re.search('[0-9,]*', points).group().replace(',', '')
        viewsRegex = re.search('[0-9,]*', views).group().replace(',', '')
        commentsRegex = re.search('[0-9,]*', comments).group().replace(',', '')

        
        #Appending metadata to CSV file
        with open(f'imgur/{subfolderName}/{self.searchTerm}-meta.csv', 'a', newline='') as file: 
            writer = csv.writer(file)
            writer.writerow([idSliced, title, author, date, pointsRegex, viewsRegex, commentsRegex,version])
        
        




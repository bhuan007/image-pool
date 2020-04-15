from bs4 import BeautifulSoup
from selenium import webdriver
import requests, os, time

# Create folder directory for images to be downloaded to
os.makedirs('imgur', exist_ok=True)

# Asking user for image search term
print('Please enter what type of image you would like to download from imgur: ')
sTerm = str(input())

# Sending a request to imgur for user's search term
res = requests.get('https://imgur.com/search/score/all?q_type=jpg&q_all=' + sTerm)

# Parsing page and selecting all images links into an array
soup = BeautifulSoup(res.text, 'html.parser')
imgArray = soup.select('a[class=image-list-link]')

browser = webdriver.Chrome()

# Looping through image array and selecting each href to higher quality image
for x in imgArray:
    imglink = x.get('href')
    pictureAddress = 'https://imgur.com' + imglink

    
    try: 
        browser.get(pictureAddress)
        time.sleep(0.5)
        imgDiv = browser.find_element_by_class_name('image-placeholder')

        imgLink = imgDiv.get_attribute('src')

        res = requests.get(imgLink)

        imageFile = open(os.path.join('imgur', os.path.basename(imgLink)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    except:
        continue

browser.quit()




# imgur-downloader
This program lets you download images and logs the image metadata to a csv from imgur.

The metadata will log: picture id, post title, name of user who uploaded, date of upload, points (upvotes), number of views, and number of comments

PREQUISITES:

1) If you don't have python 3 and pip installed, you can download it from here: https://www.python.org/downloads/


2) This program will need the Google Chrome Browser AND Chrome Webdriver to work properly. 
Download Google Chrome Browser here: https://www.google.com/chrome/

Please download your corresponding webdriver at https://sites.google.com/a/chromium.org/chromedriver/downloads. You can check which version your chrome is by clicking the three dots on the top right corner of the chrome browser window -> help -> about google chrome.

After downloading the webdriver, you will need to place the webdriver onto a specified SYSTEM path. You can either place the webdriver into a new path folder or a existing path folder.

Please view the following guides if you need help.

For windows: https://www.itprotoday.com/cloud-computing/how-can-i-add-new-folder-my-system-path

For Mac OS: https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/

For Linux: https://opensource.com/article/17/6/set-path-linux

3) After cloning or downloading the repo, make sure to run "pip install -r requirements.txt" on the terminal inside the program directory. This will download the required dependencies. *NOTE do not place the main program folder inside a folder with high level of permissions such as Program Files. The script will not be able to create a folder to store the images.

After all three steps, your program is ready to run. On the terminal, navigate to the program directory and execute the program by running "python entry.py"

The program will ask you for a search term. Go ahead and type whatever you please. An automated chrome window will pop open and will start searching and downloading the corresponding images. Do not close the window. Let the program run, the automated window will close by itself once the program is complete.

Once finished, you will have a new folder inside the program directory named 'imgur'. This is the main location of your downloaded images. Inside that main folder, you will have subfolders for each search labeled by date and search term, which will have your images and csv file enclosed inside.

CLASS USAGE:

INSTANTIATE: 

    scraper = ImgurScraper(searchTerm, downloadNum)

example:

searchTerm is what the user wants to search.

downloadNum sets the number of images to be downloaded.

    searchTerm = 'cute dogs'

    downloadNum = 70

    scraper = ImgurScraper(searchTerm, downloadNum)

METHODS:

The following will start the webscraping application
    
    scraper.scrape()

PROPERTIES:

This property returns an integer that represents how many errors occured during the downloading of images. Sometimes imgur returns gifs or videos during the search, and the program will not download those file types and include it in the errorCount.
    scraper.errorCount

example:

    if (scraper.errorCount > 0):

        print('Uh oh, there were problems with ' + str(scraper.errorCount) + ' images.')





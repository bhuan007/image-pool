# imgur-downloader
Downloads jpeg images from imgur.

PREQUISITES:

1) If you don't have python 3 installed, you can download it from here: https://www.python.org/downloads/


2) This program will need Google Chrome's Browser AND Webdriver to work properly. 
Download Google Chrome Browser here: https://www.google.com/chrome/
Please download your corresponding webdriver at https://sites.google.com/a/chromium.org/chromedriver/downloads and set the driver to your system PATH. 
You can check which version your chrome is by clicking the three dots on the top right corner of the browser window -> help -> about google chrome.

3) After cloning or downloading the repo, make sure to run "pip install -r requirements.txt" on the terminal inside the program directory. This will download the required dependencies.

After all three steps, your program is ready to run. On the terminal, execute the program by running "python imgurDownloader.py"

The program will ask you for a search term. Go ahead and type whatever you please. A artificial window will pop open and will start searching and downloading the corresponding images. Let the program run, all the windows will close once the program is complete.

Once finished, you will have a new folder inside the program directory named 'imgur'. This is the location of your downloaded images.


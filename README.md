# imgur-downloader
Downloads up to 60 jpeg images from imgur depending on your search term.

PREQUISITES:

1) If you don't have python 3 installed, you can download it from here: https://www.python.org/downloads/


2) This program will need the Google Chrome Browser AND Chrome Webdriver to work properly. 
Download Google Chrome Browser here: https://www.google.com/chrome/

Please download your corresponding webdriver at https://sites.google.com/a/chromium.org/chromedriver/downloads. You can check which version your chrome is by clicking the three dots on the top right corner of the chrome browser window -> help -> about google chrome.

After downloading the webdriver, you will need to place the webdriver onto a specified SYSTEM path. You can either place the webdriver into a new path folder or a existing path folder.

Please view the following guides if you need help.

For windows: https://www.itprotoday.com/cloud-computing/how-can-i-add-new-folder-my-system-path

For Mac OS: https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/

For Linux: https://opensource.com/article/17/6/set-path-linux

3) After cloning or downloading the repo, make sure to run "pip install -r requirements.txt" on the terminal inside the program directory. This will download the required dependencies.

After all three steps, your program is ready to run. On the terminal, execute the program by running "python imgurDownloader.py"

The program will ask you for a search term. Go ahead and type whatever you please. An automated chrome window will pop open and will start searching and downloading the corresponding images. Do not close the window. Let the program run, the automated window will close by itself once the program is complete.

Once finished, you will have a new folder inside the program directory named 'imgur'. This is the location of your downloaded images.


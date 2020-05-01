This program lets you download images and logs the image metadata to a csv from imgur.
The metadata will log: picture id, post title, name of user who uploaded, date of upload, points (upvotes), number of views, and number of comments

INSTRUCTIONS:

1. Download or clone the repo. NOTE: Do not place the main program folder inside a folder with a high level of permissions such as Program Files. The script will not be able to create a folder to store the images. We recommend placing the main program folder in C:\Users\YourName. Also make sure that your firewall does not delete the program. You could also technically delete all files except for imagePool.exe, I just included the code for anyone intersted in seeing how the program works.

**2. This program will need the Google Chrome Browser AND Chrome Webdriver to work properly. Download Google Chrome Browser here: https://www.google.com/chrome/**

**3. Please download your corresponding webdriver at https://sites.google.com/a/chromium.org/chromedriver/downloads. You can check which version your chrome is by clicking the three dots on the top right corner of the chrome browser window -> help -> about google chrome.**

4. After downloading the webdriver, you will need to unzip and place the webdriver application inside the main program folder.

5. After doing the above, your program is ready to run. Navigate to the program folder directory and execute the program by double clicking imagePool.exe

6. A terminal will open along with a graphical user interface. Please type in a search term and a number of images to be downloaded, and select whether you would want a csv file or not (for metadata collection).

7. Once finished, you will have a new folder inside the program directory named 'imgur'. This is the main location of your downloaded images. Inside that main folder, you will have subfolders for each search labeled by date and search term, which will have your images and csv file enclosed inside.

from ImgurScraper import ImgurScraper

print('What would you like to search from imgur?')

sTerm = str(input())

print('How many pictures would you want to download?')

downloadNum = int(input())

scraper = ImgurScraper(sTerm, downloadNum)

scraper.scrape()

if (scraper.errorCount > 0):
    print('Uh oh, there were problems with ' + str(scraper.errorCount) + ' images.')

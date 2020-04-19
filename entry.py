from ImgurScraper import ImgurScraper

print('What would you like to search from imgur?')

sTerm = str(input())

print('How many pictures would you want to download?')

downloadNum = int(input())

scraper = ImgurScraper(sTerm, downloadNum)

scraper.scrape()

if (scraper.errorCount > 0):
    print('There were ' + str(scraper.errorCount) + ' images that were not downloaded. This is probably because it was not a JPEG type image.')
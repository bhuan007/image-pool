from ImgurScraper import ImgurScraper

print('What would you like to search from imgur?')

sTerm = str(input())

print('How many pictures would you want to download?')

downloadNum = int(input())

while True:
    print("Would you like to generate and collect metadata to a csv file? (Y/N)")
    isOutputCSV = input().lower()

    if (isOutputCSV == 'y'):
        isOutputCSV = True
        break
    elif (isOutputCSV == 'n'):
        isOutputCSV = False
        break
    else:
        print('We did not understand your input try again.')

scraper = ImgurScraper(sTerm, downloadNum, isOutputCSV)

scraper.scrape()

if (scraper.errorCount > 0):
    print('Uh oh, there were problems with ' + str(scraper.errorCount) + ' images.')

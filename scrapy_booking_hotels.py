# Import os => Library used to easily manipulate operating systems
## More info => https://docs.python.org/3/library/os.html
import os 

# Import logging => Library used for logs manipulation 
## More info => https://docs.python.org/3/library/logging.html
import logging

# Import scrapy and scrapy.crawler 
import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    # Name of your spider
    name = "booking_hotels"

    # Chargement txt avec les URL :
    start_urls=[]
    with open('src/url_hotels_booking.txt', "r") as file:
        for ligne in file:
            start_urls.append(ligne.strip())

    # # Url to start your spider from 
    # start_urls = [
    #     'https://www.booking.com/hotel/fr/vert.fr.html?aid',
    # ]

    # Callback function that will be called when starting your spider
    # It will get text, author and tags of all the <div> with class="quote"
    def parse(self, response):
        yield {
            'hotel_name': response.xpath('/html/body/div[3]/div/div[5]/div[1]/div[1]/div[1]/div/div[3]/div[9]/div[1]/div/div/h2/text()').get(),
            'hotel_name_2': response.xpath('/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[3]/div[9]/div[1]/div/div/h2/text()').get(),
            'hotel_name_3': response.xpath('/html/body/div[4]/div/div[5]/div[1]/div[1]/div[1]/div/div[3]/div[9]/div[1]/div/div/h2/text()').get(),
            'lat_lon': response.xpath('/html/body/div[3]/div/div[5]/div[1]/div[1]/div[1]/div/div[2]/div[4]/a').get(),
            'lat_lon_2': response.xpath('/html/body/div[4]/div/div[5]/div[1]/div[1]/div[1]/div/div[2]/div[4]/a').get(),
            'lat_lon_3': response.xpath('/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[4]/a').get(),
            'hotel_description': response.xpath('/html/body/div[3]/div/div[5]/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/p/text()').get(),
            'hotel_description_2': response.xpath('/html/body/div[3]/div/div[6]/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/p/text()').get(),
            'hotel_description_3': response.xpath('/html/body/div[4]/div/div[5]/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/p/text()').get(),
        }
            
# Name of the file where the results will be saved
filename = "booking_hotels_scraping.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir('src/'):
        os.remove('src/' + filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
## More info on built-in settings => https://docs.scrapy.org/en/latest/topics/settings.html?highlight=settings#settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'src/' + filename : {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(QuotesSpider)
process.start()
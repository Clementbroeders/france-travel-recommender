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
    name = "booking_cities"

    # Chargement txt avec les URL :
    start_urls=[]
    with open('src/url_cities_booking.txt', "r") as file:
        for ligne in file:
            start_urls.append(ligne.strip())

    # # Url to start your spider from 
    # start_urls = [
    #     'https://www.booking.com/searchresults.fr.html?ss=Mont+Saint+Michel&lang=fr&sb=1&src_elem=sb&src=searchresults&checkin=2023-11-01&checkout=2023-11-02&group_adults=2&no_rooms=1&group_children=0',
    # ]

    # Callback function that will be called when starting your spider
    # It will get text, author and tags of all the <div> with class="quote"
    def parse(self, response):
        n = 50
        for i in range(n):
            i = i + 1
            yield {
                'city': response.xpath('/html/body/div[5]/div/div[4]/div[1]/div[1]/div[1]/div/div/h1/text()').get(),
                'hotel_name': response.xpath(f'/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[{i}]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a/div[1]/text()').get(),
                'url_hotel': response.xpath(f'/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[{i}]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/h3/a').get(),
                'score_given': response.xpath(f'/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]/div[{i}]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/a/span/div/div[1]/text()').get(),
            }
            
# Name of the file where the results will be saved
filename = "booking_cities_scraping.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
# if filename in os.listdir('src/'):
#         os.remove('src/' + filename)

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
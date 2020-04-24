# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.goodreads.com']
    start_urls = ['https://www.goodreads.com/']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_path = which('chromedriver')
        driver = webdriver.Chrome(executable_path=chrome_path,options=chrome_options)
        driver.set_window_size(1920,1080)
        driver.get('https://www.goodreads.com')
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for div in resp.xpath("//div[@id='quotes']/div"):
            quote = div.xpath('normalize-space(.//div[@class="quoteText"]/text())').get()
            author = div.xpath('normalize-space(.//div[@class="quoteText"]/span[@class="authorOrTitle"]/text())').get()
            yield {
                'quote': quote,
                'author': author
            }

# -*- coding: utf-8 -*-
import scrapy


class ExchangeSpider(scrapy.Spider):
    name = 'exchange'
    allowed_domains = ['www.x-rates.com']
    start_urls = ['https://www.x-rates.com/table/?from=INR&amount=1']

    def parse(self, response):
        for row in response.xpath("//table[@class='tablesorter ratesTable']/tbody/tr"):
            currency = row.xpath('.//td[1]/text()').get()
            rate = row.xpath('.//td[3]/a/text()').get()
            yield {
                'currency': currency,
                'rate': rate
            }

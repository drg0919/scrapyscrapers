# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating',headers = {
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[1]"), process_request='set_user_agent')
    )

    def set_user_agent(self,request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//div[@class='title_wrapper']/h1/span[@id='titleYear']/a/text()").get(),
            'rating': response.xpath("//div[@class='ratingValue']/strong/span/text()").get(),
            'run_time': response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
            'rated': response.xpath("normalize-space(//div[@class='subtext']/text())").get(),
            'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get()
        }

# -*- coding: utf-8 -*-
import scrapy


class PositiveBreakoutsSpider(scrapy.Spider):
    name = 'positive_breakouts'
    allowed_domains = ['www.moneycontrol.com']
    start_urls = ['https://www.moneycontrol.com/technicals/breakout/positive/avg30/index.html']

    def parse(self, response):
        for row in response.css('tr'):
            title = row.xpath('.//td[1]/a/b/text()').get()
            link = response.urljoin(row.xpath('.//td[1]/a/@href').get())
            if not title:
                continue
            current_price = row.xpath('.//td[2]/text()').get()
            change = row.xpath('.//td[3]/text()').get()
            sma_30 = row.xpath('.//td[4]/text()').get()
            sma_50 = row.xpath('.//td[5]/text()').get()
            sma_150 = row.xpath('.//td[6]/text()').get()
            sma_200 = row.xpath('.//td[7]/text()').get()
            data = {"title": title, "current": current_price, "change":change, "sma_30": sma_30, "sma_50": sma_50, "sma_150": sma_150, "sma_200": sma_200, "link": link}
            yield response.follow(url=link,callback=self.parse_page,meta={'tempdata':data})
        
    def parse_page(self,response):
        link = response.urljoin(response.xpath('//dt[@class="home"]/a/@href').get())
        data = response.request.meta['tempdata']
        yield response.follow(url=link,callback=self.parse_ratio,meta={'tempdata': data})

    def parse_ratio(self,response):
        pe_ratio = response.xpath('//div[@id="standalone_valuation"]/ul/li[1]/ul/li[2]/div[@class="value_txtfr"]/text()').get()
        ind_pe = response.xpath('//div[@id="standalone_valuation"]/ul/li[2]/ul/li[2]/div[@class="value_txtfr"]/text()').get()
        data = response.request.meta['tempdata']
        final_data = {}
        for (key,value) in data.items():
            if key != 'link':
                final_data[key] = value
        final_data['pe_ratio'] = pe_ratio
        final_data['ind_pe'] = ind_pe
        final_data['link'] = data['link']
        yield final_data
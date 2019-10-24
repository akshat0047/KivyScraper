# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from scrapy.loader import ItemLoader
from scrape.items import Headers




'''
# replace with .Firefox(), or with the browser of your choice
browser = webdriver.Firefox()
url = "https://zoylo.com"
browser.get(url)

innerHTML = browser.execute_script("return document.body.innerHTML")
'''


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


class HeadersSpider(scrapy.Spider):
    name = 'headers'
    data_list = []
    start_urls = ['https://underdogs.cf']

    def parse(self, response):
        l = ItemLoader(item=Headers(), response=response)

        h1 = response.xpath('//h1').extract()
        h2 = response.xpath('//h2').extract()
        h3 = response.xpath('//h3').extract()
        h4 = response.xpath('//h4').extract()
        h5 = response.xpath('//h5').extract()

        data = {"url": response.url, "h1": h1,
                "h2": h2, "h3": h3, "h4": h4, "h5": h5}
        for x in data.values():
            if type(x) is not str:
                for i in range(0, len(x)):
                    x[i] = striphtml(x[i])
                    x[i] = x[i].strip()

        # Loading Item
        l.add_value('url', data['url'])
        l.add_value('h1', data['h1'])
        l.add_value('h2', data['h2'])
        l.add_value('h3', data['h3'])
        l.add_value('h4', data['h4'])
        l.add_value('h5', data['h5'])

        #self.data_list.append(data)
        #print(self.data_list)

        return l.load_item()

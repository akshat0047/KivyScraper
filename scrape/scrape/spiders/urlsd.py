import scrapy
from scrapy.linkextractors import LinkExtractor
import tldextract


class UrlsDSpider(scrapy.Spider):
    name = 'urlsd'
    dom = ''

    def __init__(self, *args, **kwargs):
        super(UrlsDSpider, self).__init__(*args, **kwargs)
        # custom_settings = {
        #    'DEPTH_LIMIT': int(kwargs.get('meta')['depth'])
        # }
        self.dom = tldextract.extract(kwargs.get('meta')['url'])
        # print(self.dom)
        self.start_urls = [kwargs.get('meta')['url'], ]

    def parse(self, response):
        le = LinkExtractor(allow_domains=(
            self.dom.domain + "." + self.dom.suffix,))
        self.data_list.append(response.url)
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse)

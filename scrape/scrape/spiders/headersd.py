import scrapy
from scrapy.linkextractors import LinkExtractor
import tldextract
import re
import csv
from scrapy import signals
from scrapy.loader import ItemLoader
from scrape.items import Headers

# DOMAIN = 'www.americanexpress.com'
# URL = 'http://%s' % DOMAIN
# header_list = []


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


class HeadersDSpider(scrapy.Spider):
    name = 'headersd'
    dom = ''
    start_urls = ['https://underdogs.cf']
    data_list = []

    def __init__(self, *args, **kwargs):
        super(HeadersDSpider, self).__init__(*args, **kwargs)
        self.dom = tldextract.extract(self.start_urls[0])

        # custom_settings = {
        #    'DEPTH_LIMIT': kwargs.get('meta')['depth']
        # }

    def parse(self, response):
        self.l = ItemLoader(item=Headers(), response=response)
        if response.status not in [404, 500]:

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
            # print(data)
            self.data_list.append(data)

            le = LinkExtractor(allow_domains=(
                self.dom.domain + "." + self.dom.suffix,), unique=True, deny="#+")
            for link in le.extract_links(response):

                yield scrapy.Request(link.url, callback=self.parse)

        self.l.add_value('url', data['url'])
        self.l.add_value('h1', data['h1'])
        self.l.add_value('h2', data['h2'])
        self.l.add_value('h3', data['h3'])
        self.l.add_value('h4', data['h4'])
        self.l.add_value('h5', data['h5'])

        yield self.l.load_item()

        '''
        csv_columns = ['url', 'h1', 'h2', 'h3', 'h4', 'h5']
        try:
            with open('zoyoloRs.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in self.data_list:
                    writer.writerow(data)

        except IOError:
            print("I/O error")
        '''

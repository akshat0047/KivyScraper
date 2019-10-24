# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
from scrape import settings


def write_to_csv(item):
    print("Im in")
    csv_columns = ['url', 'h1', 'h2', 'h3', 'h4', 'h5']
    try:
        with open('zoyolo.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            writer.writerow(item)

    except IOError:
        print("I/O error")


class WriteToCsv(object):
    def process_item(self, item, spider):
        write_to_csv(item)
        return item

# -*- coding: utf-8 -*-
import scrapy
import csv
import json

class DataGovSpider(scrapy.Spider):
    name = 'data_gov'
    start_urls = ['http://data.gov.ph/search/type/dataset']

    def parse(self, response):
        pass

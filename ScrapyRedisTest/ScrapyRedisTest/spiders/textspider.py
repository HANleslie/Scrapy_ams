# coding=utf-8
from scrapy import Spider

class testcrawl(Spider):
    name = 'testcrawl'
    start_urls = ['https://www.baidu.com',]
    def parse(self,response):
        print(response.headers)
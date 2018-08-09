# coding=utf-8

from ScrapyRedisTest.scrapy_redis.spiders import RedisSpider

class JobBolespider(RedisSpider):
    name = 'jobbole'
    allowed_domain = ['blog.jobbole.com']
    redis_key = 'jobbole:start_urls'

    def parse(self,response):
        pass
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
from .settings import User_Agent

class ScrapyredistestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyredistestDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class MyUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        ua = random.choice(User_Agent)
        if ua:
            request.headers['User-Agent'] = ua
            request.headers['Cookie'] = '_ga=GA1.2.971917165.1524722785; user_trace_token=20180426140629-f61ccc8d-4917-11e8-a53a-525400f775ce; LGUID=20180426140629-f61cd073-4917-11e8-a53a-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; fromsite="localhost:49228"; index_location_city=%E4%B8%8A%E6%B5%B7; JSESSIONID=ABAAABAAADEAAFI9701AC4E02A11864C939571664DA8BC9; _gid=GA1.2.1070412789.1533448525; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533209375,1533211532,1533289026,1533448526; LGSID=20180805135526-26484754-9874-11e8-a339-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_user; X_HTTP_TOKEN=630011e21add5442e33c65788829f424; LG_LOGIN_USER_ID=25dc26c4e7372772b251fb751357d4a0a2c3ea33380bad1dfa6022f3409e364e; _putrc=CF10CD86D8BF84A8123F89F2B170EADC; login=true; unick=%E9%9F%A9%E6%A2%A6%E6%B4%81; gate_login_token=91388ece0bb3568c6844df8c17802c081182fd1d8b1444c72ca9ace216763b7e; LGRID=20180805135558-39833a1e-9874-11e8-b617-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533448558'


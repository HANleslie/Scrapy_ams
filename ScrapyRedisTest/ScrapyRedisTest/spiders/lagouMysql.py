# coding=utf-8
from ..scrapy_redis.spiders import RedisSpider,RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from ..items import LagouItem,LagouItemLoader
import datetime

class lagouMysql(RedisCrawlSpider):
    name = 'lagoumysqlcrawl'
    redis_key = 'lagoumysqlcrawl:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        # domain = kwargs.pop('domain', '')
        # self.allowed_domains = filter(None, domain.split(','))

        # 修改这里的类名为当前类名
        super(lagouMysql, self).__init__(*args, **kwargs)

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_lagou_process', follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html\?source=pl&i=pl-0'), callback='parse_lagou_process', follow=True),

    )

    def parse_lagou_process(self, response):
        item_loader = LagouItemLoader(item=LagouItem(), response=response)
        item_loader.add_xpath("title", "//div[@class='position-head']//span[@class='name']/text()")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_md5", response.url)
        item_loader.add_xpath("salary",
                              "//div[@class='position-content-l']//dd[@class='job_request']/p//span[1]/text()")

        item_loader.add_xpath("career_exprience",
                              "//div[@class='position-content-l']//dd[@class='job_request']/p//span[3]/text()")

        item_loader.add_xpath("education",
                              "//div[@class='position-content-l']//dd[@class='job_request']/p//span[4]/text()")
        item_loader.add_xpath("employed_type",
                              "//div[@class='position-content-l']//dd[@class='job_request']/p//span[5]/text()")
        item_loader.add_xpath("job_label", "//ul[@class='position-label clearfix']/li/text()")
        item_loader.add_xpath("publish_time", "//p[@class='publish_time']/text()")
        item_loader.add_xpath("job_requirements", "//dl[@id='job_detail']/dd[@class='job_bt']")
        item_loader.add_xpath("company_addr", "//div[@class='work_addr']")

        item_loader.add_xpath("company_name", "//dl[@id='job_company']/dt/a/div[1]/h2/text()")
        item_loader.add_xpath("company_scale", "//i[@class='icon-glyph-figure']/following-sibling::text()")
        item_loader.add_xpath("compay_websit", "//dl[@id='job_company']/dt/a/@href")
        item_loader.add_xpath("company_label", "//i[@class='icon-glyph-fourSquare']/following-sibling::text()")
        # "//ul[@class='c_feature']//li[1]/text()"
        item_loader.add_value("crawl_time", str(datetime.datetime.now())[:10])
        item_loader.add_value("crawl_update_time", str(datetime.datetime.now())[:10])

        Lagouitem = item_loader.load_item()

        return Lagouitem
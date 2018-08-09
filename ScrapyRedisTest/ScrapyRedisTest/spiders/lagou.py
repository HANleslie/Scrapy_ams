# coding=utf-8
# from scrapy_redis.spiders import RedisSpider
from ..scrapy_redis.spiders import RedisSpider
from scrapy.spiders import Request
from ..items import Job51CrawlItem

class lagoucrawl(RedisSpider):
    name = 'lagoucrawl'
    redis_key = 'lagoucrawl:start_urls'

    url_pre = 'https://m.51job.com/search/joblist.php?jobarea=040000&keyword=%E7%88%AC%E8%99%AB&keywordtype=2&pageno=1'

    def start_requests(self):
        yield Request(url=self.url_pre, callback=self.parse_list_page)

    def parse_list_page(self, response):

        specify_page = response.xpath("//div[@id='pageContent']//div[@class='items'][1]/a/@href").extract()

        for each_url in specify_page:
            print(each_url)
            yield Request(each_url, callback=self.parse_spicify_page)

        for i in range(0, 106):
            yield Request(self.url_pre.format(pag=str(i)), self.parse_list_page)

    def parse_spicify_page(self,response):
        Item = Job51CrawlItem()
        Item['title'] = response.xpath("//div[@id='pageWp']//div[@class='mod m1']/div[@class='jt']/p/text()").extract()
        Item['salary'] = response.xpath("//div[@id='pageWp']//div[@class='mod m1']/p[@class='jp']/text()").extract()
        Item['release_time'] = response.xpath("//div[@id='pageWp']//div[@class='mod m1']/div[@class='jt']/span/text()").extract()
        Item['area_localtion'] = response.xpath("//div[@id='pageWp']//div[@class='mod m1']/div[@class='jt']/em/text()").extract()
        Item['requirement_number'] = response.xpath("//div[@id='pageWp']//div[@class='mod m1']/div[@class='jd']/span[@class='s_r']/text()").extract()
        Item['education'] = response.xpath("//div[@id='pageWp']//div[@class='mod m1']/div[@class='jd']/span[@class='s_x']/text()").extract()
        Item['com_link'] = response.xpath("//div[@id='pageWp']//div[@class='rec']/a/@href").extract()
        Item['company'] = response.xpath("//div[@id='pageWp']//div[@class='rec']/a/p[@class='c_444']/text()").extract()
        Item['company_intruduce'] = response.xpath("//div[@id='pageWp']//div[@class='rec']/a/div[@class='at']/text()").extract()
        Item['company_addr'] = response.xpath("//div[@id='pageWp']//div[@class='rec']/a[@class='arr a2']/span/text()").extract()
        Item['company_addr_mapurl'] = response.xpath("//div[@id='pageWp']//div[@class='rec']/a[@class='arr a2']/@href").extract()
        Item['position_discribe'] = response.xpath("//div[@id='pageWp']//div[@class='mod']/div[@class='ain']/article//p/text()").extract()
        Item['label'] = response.xpath("//div[@id='pageWp']//div[@class='mod']/div[@class='welfare']//span/text()").extract()

        yield Item
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import hashlib,re
from lxml import etree
from time import time,gmtime

from scrapy import Item,Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class ScrapyredistestItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Job51CrawlItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    release_time = Field()
    salary = Field()
    area_localtion = Field()
    requirement_number = Field()
    education = Field()
    experience_requirement = Field()
    company = Field()
    com_link = Field()
    company_intruduce = Field()
    company_addr = Field()
    company_addr_mapurl = Field()
    company_scale = Field()
    position_discribe = Field()
    benefits = Field()
    label = Field()


def encrymd5(value):

    if len(value):
        h = hashlib.md5()
        h.update(value.encode(encoding='utf-8'))
        return h.hexdigest()
    else:
        return None


def wipe_split(value):
    value = value.strip(' /')
    return value

def wipe_enter(value):
    value = value.strip(' \n')
    return value

def wipe_blank(value):
    value = value.replace('\xa0','')
    return value

def com_addr_handle(value):
    html = etree.HTML(value.replace('\n',''))
    result = html.xpath("//text()")
    result = ''.join([i.strip(' ') for i in result])
    return result[:-4]

def publish_time_handle(value):
    # 判断两种情况
    if re.match('\d{4}-\d{1,2}-\d{1,2}',value):
        return value
    else:
        JD1 = re.findall("(\d{2}:\d{2})", value)
        JD2 = re.findall("(\d+)", value)
        # 08:29  发布于拉勾网
        if JD1 != []:
            result =  time()
        # 2天前  发布于拉勾网
        elif JD2 != [] and JD1 == []:
            result = time() + int(JD2[0]) * 24 * 3600
        else:
            return None
        return ('-'.join([str(i) for i in [gmtime(result)[0], gmtime(result)[1], gmtime(result)[2]]]))

def process_longtext(value):

    return value.replace(',','>').replace('\'',':').replace('\"','')



class LagouItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class LagouItem(Item):
    title = Field()
    url = Field()
    url_md5 = Field(
        input_processor = MapCompose(encrymd5),
    )
    salary = Field()
    salary_low = Field()
    salary_upper = Field()
    career_exprience = Field(
        input_processor = MapCompose(wipe_split),
    )
    career_exprience_low = Field()
    career_exprience_upper = Field()
    education = Field(
        input_processor = MapCompose(wipe_split)
    )
    employed_type = Field()
    job_label = Field()
    publish_time = Field(
        input_processor = MapCompose(publish_time_handle)
    )
    job_requirements = Field(
        input_processor = MapCompose(process_longtext)
    )
    company_addr = Field(
        input_processor=MapCompose(com_addr_handle)
    )
    company_addr_city = Field()
    company_addr_area = Field()
    company_addr_detail = Field()
    company_name = Field(
        input_processor = MapCompose(wipe_enter)
    )
    company_scale = Field(
        input_processor = MapCompose(wipe_enter)
    )
    compay_websit = Field()
    company_label = Field(
        input_processor = MapCompose(wipe_enter)
    )
    crawl_time = Field()
    crawl_update_time = Field()
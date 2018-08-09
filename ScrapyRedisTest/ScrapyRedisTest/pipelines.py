# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,pymysql,re



class ScrapyredistestPipeline(object):
    def process_item(self, item, spider):
        return item

class Job51DumpJsonPipeline(object):

    def open_spider(self,sipder):
        self.file = open('liepin.txt','w',encoding='utf-8')
        print('open the liepin.txt')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item),indent=4,ensure_ascii=False))
        return item

    def close_spider(self,spider):
        self.file.close()
        print('close the liepin.txt')


class LagouItemProcess(object):
    def process_item(self,item,spider):
        if item['career_exprience']:
            res_exp = re.findall("(\d+-\d+)", item['career_exprience'])
            if res_exp:
                item['career_exprience_low'] = int(res_exp[0].split('-')[0])
                item['career_exprience_upper'] = int(res_exp[0].split('-')[1])
        if item['salary']:
            res_salar = item['salary'].replace('k','')
            res_salar = re.findall("(\d+-\d+)", res_salar)
            if res_salar:
                item['salary_low'] = int(res_salar[0].split('-')[0])
                item['salary_upper'] = int(res_salar[0].split('-')[1])
        if item['company_addr']:
            item['company_addr'] = item['company_addr'].split('-')
            item['company_addr_city'] = item['company_addr'][0]
            item['company_addr_area'] = ' '.join(item['company_addr'][1:-1])
            item['company_addr_detail'] = item['company_addr'][-1]


        return item

class MySQLdbTest(object):

    def __init__(self):
        self.db = pymysql.connect('10.36.132.127','guest','123','jobbole_test')
        self.conn = self.db.cursor()

    def process_item(self,item,spider):

        sql = """
            INSERT INTO lagou(title,url,url_md5) VALUES ( %s,%s,%s)

        """
        try:
            self.conn.execute(sql,(item['title'],item['url'],item['url_md5']))
            self.db.commit()
            print('插入数据成功')
        except:
            self.db.rollback()
            self.db.close()
            print('插入数据失败')
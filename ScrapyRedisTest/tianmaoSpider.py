# coding=utf-8

import requests,re,json
from lxml import etree

def get_url(url):
    response = requests.get(url)
    if response.status_code==200:
        html = etree.HTML(response.text)
        res = html.xpath("//div[@class='product  ']/@data-id")
        for prefix in res:
            url = 'https://detail.tmall.hk/hk/item.htm?id=' + prefix
            yield url


        # with open('tianmao.html','w',encoding='utf-8') as f:
        #     f.write(response.text)
        # res = re.findall('.*\{(.*)\}.*',response.text)[0]
        # for item in res.split(':'):
        #     if 'id' in item:
        #         print(item)
        # print(res)
        # print(re.findall("https:\/\/detail.tmall.com\/item.htm?id=(\d+)",res))
        # print(json.loads(re.findall('.*\{(.*)\}.*',response.text)[0]))
        # with open('tianmao.json','w',encoding='utf-8') as f:
        #     f.write(json.dumps(re.findall('.*\{(.*)\}.*',response.text)[0]))
        # print()

    else:
        print(response.status_code)

def get_data(url):

    response = requests.get(url)
    if response.status_code==200:
        html = etree.HTML('//title/text()')
        print(html)


if __name__ == '__main__':
    # url = 'https://tmatch.simba.taobao.com/?name=tbuad&ismall=1&o=j&pid=419108_1006&count=5&keyword=%D2%BB%B6%CE%C4%CC%B7%DB&p4p=tbcc_p4p_c2016_8_131194_15335430304731533543030863&sbid=1'
    url = 'https://list.tmall.com/search_product.htm?spm=a221w.7782398.100007.1.79502631VAFV5L&acm=lb-zebra-19604-297596.1003.8.431292&vmarket=&q=%D2%BB%B6%CE%C4%CC%B7%DB&from=baby..pc_1_searchbutton&type=p&scm=1003.8.lb-zebra-19604-297596.ITEM_14419407708211_431292'
    for url in get_url(url):
        print(url)
        get_data(url)

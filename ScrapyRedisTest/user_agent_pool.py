# coding=utf-8


import requests,json
from lxml import etree

def get_data(url):

    response = requests.get(url)

    if response.status_code == 200:
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        value = html.xpath("//td[@class='useragent']/text()")
        key = html.xpath("//td[@class='system']")
        # print(value)

        return value,key

def userAgentDic(value,key):
    new_value = []
    # new_key = []
    # for item in key:
    #     new_key.append(''.join(item.xpath("text()")).replace('\xa0',' '))
    #
    # uaDic = {}
    # if len(value) == len(new_key):
    #     for index in range(len(value)):
    #         uaDic[new_key[index]] = value[index]
    #     return uaDic
    # else:
    #     print('数据错误')
    for item in value:
        new_value.append(item +'\n')
    return new_value



if __name__ == '__main__':
    url = 'https://techblog.willshouse.com/2012/01/03/most-common-user-agents/'
    value,key = get_data(url)
    # uaDic = userAgentDic(value,key)
    new_value = userAgentDic(value,key)
    print(new_value)
    # with open('userAgentlist.text','w',encoding='utf-8') as f:
    #     f.write(key)
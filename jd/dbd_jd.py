# coding=utf-8
# 此程序主要抓取夺宝岛按结束时间排序的首页

import time
import re
import urllib2
import sql


def init():
    """
     # URL中sortField参数是设置排序方式
    :return: 返回夺宝岛按照结束时间排序的拍卖物品网页id
    """
    url = 'http://dbd.jd.com/auctionList.html?&auctionType=0&sortField=2&recordType=1&searchForTitle=&productCateId=&productLocation=&searchParam='
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    html = response.read()
    r = re.compile(r'paimaiIds.push\((.*?)\);')
    id_list = r.findall(html)
    return id_list
    # for id_num in id_list:
    # print id_num


def id_handle(id_num):
    """
    处理夺宝岛网页，返回处理结果
    :param id_num: 需要处理的夺宝岛物品网页id
    :return: 
    """
    r_dict = {}
    url = 'http://dbditem.jd.com/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 Safari/537.36'}

    # 下面函数获取价格
    price_json_url = 'http://dbditem.jd.com/services/currentList.action?paimaiIds=' + str(id_num) + '&callback=jsonp_1508995117024'
    # print price_json_url
    # 封顶价json网址
    maxprice_json_url = 'http://dbditem.jd.com/json/current/queryJdPrice?paimaiId=' + str(id_num)
    maxprice_request = urllib2.Request(maxprice_json_url, headers=header)
    request_price = urllib2.Request(price_json_url, headers=header)
    response_price = urllib2.urlopen(request_price)
    response_maxprice = urllib2.urlopen(maxprice_request)

    # maxprice最高价
    maxprice_html = response_maxprice.read()
    re_maxprice = re.compile(r':(.*?),')
    maxprice = re_maxprice.findall(maxprice_html)

    # price 获取商品价格
    price_html = response_price.read()
    re_price = re.compile(r'currentPrice":(.*?),"')
    price = re_price.findall(price_html)

    # 下面代码是提取夺宝岛物品名称
    request_name = urllib2.Request(url + str(id_num), headers=header)
    response_name = urllib2.urlopen(request_name)
    html = response_name.read()
    r_name = re.compile(r'title="(.*?)">')
    r_old_new = re.compile(r'class="useIcon(.*?)"')
    r_time = re.compile(r'<span class="color33">(.*?)<')
    # 附件寻找的正则表达式
    r_appendix = re.compile(r'<span class="item_accessory_info">(.*?)<')

    time.sleep(0.3)

    title_name = r_name.findall(html)
    title_time = r_time.findall(html)
    new_old = r_old_new.findall(html)
    # 附件
    title_appendix = r_appendix.findall(html)

    # print int(new_old[0])
    # print title_name[0]
    try:
        return title_name[0], new_old[0], price[0], maxprice[0], title_appendix[0], title_time[0]
    except Exception, e:
        print e.message
        print 'Handle error!'


def inster_sql(id_list):
    """
    向mysql添加数据
    :param id_list: 即将拍卖物品的列表
    :return: 
    """
    for price_id in id_list:
        goods_list = id_handle(price_id)
        print price_id
        if goods_list:
            # for goods in goods_list:
            #     print goods, type(goods)

            find_result = sql.find_data((goods_list[0],))
            if find_result:

                sql.insert_list((int(price_id), int(find_result), int(goods_list[1]), int(float(goods_list[2])), int(float(goods_list[3])), goods_list[4], goods_list[5]))
                print 'Insert list ok!'
            else:
                sql.insert_goods(goods_list[0])
                find_result2 = sql.find_data((goods_list[0],))
                if find_result2:
                    try:
                        sql.insert_list((int(price_id), int(find_result), int(goods_list[1]), int(float(goods_list[2])),
                                         int(float(goods_list[3])), goods_list[4], goods_list[5]))
                        print 'Insert list OK!'
                    except Exception, e:
                        print e.message


if __name__ == '__main__':
    id_list = init()
    diy_list = (i for i in range(9556864, 16903199))
    inster_sql(diy_list)









# coding=utf-8
# name=hu_yang_jie
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import urllib2
import re
import dbd_jd
import winsound


def init():
    driver = webdriver.PhantomJS()
    driver.get('https://passport.jd.com/new/login.aspx')
    ac_longin = driver.find_element_by_xpath('//div[@class="login-tab login-tab-r"]/a')
    ac_click = driver.find_element_by_id('loginsubmit')
    dr = ActionChains(driver)
    dr.click(ac_longin).perform()
    time.sleep(0.5)
    driver.find_element_by_id('loginname').send_keys(u'hyjayyw')
    driver.find_element_by_id('nloginpwd').send_keys(u'13832187106wat')
    time.sleep(0.1)
    dr.click(ac_click).perform()
    time.sleep(6)
    driver.save_screenshot('before_login.png')
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookie)
    driver.quit()
    print 'Get cookiestr OK!'
    return cookiestr


def bid(cookiestr, paimaiid, price):
    url = 'http://dbditem.jd.com/services/bid.action?t=045930&paimaiId=' + str(paimaiid) + '&price=' + str(price) + '&proxyFlag=0&bidSource=0'
    # print url
    header = {
        "Host" : "dbditem.jd.com",
        "Connection" : "keep-alive",
        # "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "Referer" : "http://dbditem.jd.com/16817459",
        #"Accept-Encoding" : "gzip, deflate, sdch",
        "Cookie" : cookiestr,
        "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6"
    }
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    print response.read()


def get_price_time(goods_id, time_str1, time_str2):
    # time_str1, time_str2 = str(int(time.time()*1000)), str(int(time.time()*1000)+2)
    url = 'http://bid.jd.com/json/current/englishquery?skuId=0&start=0&end=9&paimaiId='+str(goods_id)+'&callback=jsonpCallBack_' + time_str1 + '&_=' + time_str2
    url2 = 'http://bid.jd.com/json/current/englishquery?skuId=0&start=0&end=9&paimaiId=16853684&callback=jsonpCallBack_1510723084946&_=1510723084948'
    # print url
    header = {
        'Accept' : '*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection':'keep-alive',
        'Cookie':'__jdv=122270672|direct|-|none|-|1510063478868; user-key=c29ee9b3-e663-4114-9621-6541d5a74950; cn=21; ipLoc-djd=1-72-4137-0; areaId=1; wlfstk_smdl=qvhyjrzur3eqfdwmgrq0dtwk8mnu4xhu; _jrda=3; TrackID=1axbnbrTrRu46a6chJw0vbA5KLufvWbeq8UMNGlIPeXwcMh2S5x8kLxxpqoeAGSp8vl0yCWfg2tZf_yEA0BaS8Q; pinId=LLOpiU-2E5s; pin=hyjayyw; unick=hyjayyw; _tp=Ed%2F1DCyR3XxMhGAcG4O2uA%3D%3D; _pst=hyjayyw; ceshi3.com=103; thor=DD61B49A434FFD5C8A176FA45ACC4B92E008300201377034E12252EC283FE1BF175A78AE3648E5F227A2B0ACD898A8AF88C3E7DA0468ECFF449FFBEDFF54B81693821D77AC06EA4961477AA4F1B8DE0EED7B30E7EA7D2111EFDBB489BC4A29E122BE9DDE2659E0D20F2CAA8DC8EE01EF36DDF0D17ED2D57A2AAEDDCC9D77A6E565816FEFF25D18BB1E91B50AD7D42A2B; __jdu=634327104; 3AB9D23F7A4B3C9B=K2POWY4CWIUBF5SLKFATA5EGGAPN6XNX76JJLS7YJHEI2ATCHYMTFOCQSVQTWSKUJWCDUK3OMU6YUTBA74RBNERLJ4; __jda=122270672.634327104.1510061050.1510720336.1510727614.33; __jdb=122270672.8.634327104|33.1510727614; __jdc=122270672',
        'Host':'bid.jd.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    request_get = urllib2.Request(url, headers=header)
    response_get = urllib2.urlopen(request_get)
    html_get = response_get.read()
    # print html_get
    r_time = re.compile('remainTime":"(.*?)"')
    r_price = re.compile('currentPrice":"(.*?)"')
    time_get = r_time.findall(html_get)[0]
    price_get = r_price.findall(html_get)[0]

    # print time_get
    # print price_get
    return int(time_get), int(price_get)


def doit(pid, price_num, cookiestr):
    time_str1, time_str2 = str(int(time.time() * 1000)), str(int(time.time() * 1000) + 2)
    # cookiestr = init()

    while True:
        r_time, n_price = get_price_time(pid, time_str1, time_str2)
        if r_time < 1300 and n_price <= price_num:
            bid(cookiestr, pid, n_price+1)
            print 'ok or not'
            winsound.Beep(600, 5000)
            break
        print r_time,  n_price
        if r_time > 2500:
            time.sleep(int(r_time) / 3000)
        if r_time == -1:
            break

if __name__ == "__main__":
    count = 1
    # cookiestr = init()

    # doit(16907443, 135, cookiestr)

    # while True:
    #     id_list = dbd_jd.init()
    #     for gid in id_list:
    #         result = dbd_jd.id_handle(gid)
    #         if result:
    #             # print result[0]
    #             if '荣耀运动蓝牙耳机xSport AM61' in result[0]:
    #                 print result[0]
    #                 doit(id, 105, cookiestr)
    #     print count
    #     count = count + 1
    #     time.sleep(90)




# coding:utf-8
# name=hu_yang_jie
import time
import urllib2

for i in range(3):
    url = 'http://bid.jd.com/json/current/englishquery?skuId=0&start=0&end=9&paimaiId=16855950&callback=jsonpCallBack_1510729570061&_=1510729570062'
    header = {
        'Accept' : '*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection':'keep-alive',
        'Cookie':'__jdv=122270672|direct|-|none|-|1510063478868; user-key=c29ee9b3-e663-4114-9621-6541d5a74950; cn=21; ipLoc-djd=1-72-4137-0; areaId=1; wlfstk_smdl=qvhyjrzur3eqfdwmgrq0dtwk8mnu4xhu; _jrda=3; TrackID=1axbnbrTrRu46a6chJw0vbA5KLufvWbeq8UMNGlIPeXwcMh2S5x8kLxxpqoeAGSp8vl0yCWfg2tZf_yEA0BaS8Q; pinId=LLOpiU-2E5s; pin=hyjayyw; unick=hyjayyw; _tp=Ed%2F1DCyR3XxMhGAcG4O2uA%3D%3D; _pst=hyjayyw; ceshi3.com=103; thor=DD61B49A434FFD5C8A176FA45ACC4B92E008300201377034E12252EC283FE1BF175A78AE3648E5F227A2B0ACD898A8AF88C3E7DA0468ECFF449FFBEDFF54B81693821D77AC06EA4961477AA4F1B8DE0EED7B30E7EA7D2111EFDBB489BC4A29E122BE9DDE2659E0D20F2CAA8DC8EE01EF36DDF0D17ED2D57A2AAEDDCC9D77A6E565816FEFF25D18BB1E91B50AD7D42A2B; __jdu=634327104; 3AB9D23F7A4B3C9B=K2POWY4CWIUBF5SLKFATA5EGGAPN6XNX76JJLS7YJHEI2ATCHYMTFOCQSVQTWSKUJWCDUK3OMU6YUTBA74RBNERLJ4; __jda=122270672.634327104.1510061050.1510720336.1510727614.33; __jdb=122270672.8.634327104|33.1510727614; __jdc=122270672',
        'Host':'bid.jd.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    html = response.read()
    print html
    time.sleep(1)

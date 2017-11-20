# coding=utf-8
# name=hu_yang_jie
from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time
import handle_two_img


if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get('https://passport.bilibili.com/login')
    print driver.title
    driver.find_element_by_id('login-username').send_keys(u'18031266198')
    driver.find_element_by_id('login-passwd').send_keys(u'hyj#13180083149')
    while True:
        try:
            print 'Try find element.'
            # ac_slider 就是滑块元素
            ac_slider = driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
            # # 滑轨元素
            # ac_guide = driver.find_element_by_xpath('//div[@class="gt_guide_tip gt_show"]')
            # # 滑块滑轨底层元素
            # ac_curtain = driver.find_element_by_xpath('//div[@class="gt_curtain_tip gt_hide"]')
            # 小锁元素
            # ac_ajax = driver.find_element_by_xpath('//div[@class="gt_ajax_tip gt_ready"]')
            # print ac_slider.location
            # print ac_guide.location
            # print ac_curtain.location
            # print ac_ajax.location
            print 'Find all.********************'
            break
        except:
            time.sleep(1)
            print 'Not find slider.'
    dr1 = ActionChains(driver)
    dr1.move_to_element(ac_slider).pause(0.5).perform()
    time.sleep(1.1)
    driver.save_screenshot('1.png')
    # move_by_offset是基于当前元素坐标的位移
    dr1.click_and_hold(ac_slider).move_by_offset(198, 0).pause(0.2).perform()
    # dr1.reset_actions()方法很重要——重置操作
    time.sleep(0.5)
    file_name = '2.png'
    driver.save_screenshot(file_name)
    im = Image.open(file_name)
    im2 = Image.open('1.png')
    box = (562, 224, 822, 340)
    region = im.crop(box)
    region2 = im2.crop(box)
    im_cut1 = 'cut1.png'
    im_cut2 = 'cut2.png'
    region.save(im_cut1)
    region2.save(im_cut2)
    move_num = handle_two_img.handle_img(im_cut1, im_cut2)
    print 'move_num:', move_num

    dr1.reset_actions()
    dr1.click_and_hold(ac_slider).move_by_offset(move_num-7, 0).pause(0.1).release().perform()
    while True:
        try:
            login_lock = driver.find_element_by_xpath('//div[@class="gt_ajax_tip gt_success"]')
            print('SUCCESS')
            break
        except:
            pass

    time.sleep(0.5)
    driver.save_screenshot('3.png')

    time.sleep(4)
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookie)
    print cookiestr
    driver.quit()

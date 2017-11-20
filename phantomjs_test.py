# coding=utf-8
# name=hu_yang_jie
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from PIL import Image
import handl


def handle_driver(driver, ac1):
    dr = ActionChains(driver)
    dr.move_to_element(ac1).click_and_hold(ac1).perform()
    time.sleep(2.5)
    dr.move_by_offset(573, 381).perform()
    time.sleep(0.3)
    file_name = 'bi.png'
    driver.save_screenshot(file_name)
    # dr.release().perform()
    driver.save_screenshot('bi2.png')
    im = Image.open(file_name)
    box = (562, 224, 822, 340)
    region = im.crop(box)
    # region.show()
    file_cut = 'cut.png'
    region.save(file_cut)
    time.sleep(1)
    move_num = handl.scan_img(file_cut)
    print move_num
    # ActionChains(driver).drag_and_drop_by_offset(ac1, move_num-7, 0).perform()
    # time.sleep(1)
    # dr.move_to_element(ac1).perform()
    driver.save_screenshot('bi3.png')
    dr.move_by_offset(0, 768).release().perform()
    driver.save_screenshot('biok.png')
    time.sleep(1)
    driver.save_screenshot('biok2.png')
    dr.drag_and_drop_by_offset(ac1, 0, move_num-7).perform()
    driver.save_screenshot('biok3.png')
    driver.quit()

if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get('https://passport.bilibili.com/login')
    driver.find_element_by_id('login-username').send_keys(u'18031266198')
    driver.find_element_by_id('login-passwd').send_keys(u'hyj#13180083149')
    time.sleep(5)
    # ac1就是验证滑动块的标记
    ac1 = driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
    # 获取ac1的xy坐标值
    # ac1_x, ac1_y = int(ac1.location['x']), int(ac1.location['y'])
    # print ac1_x, ac1_y
    handle_driver(driver, ac1)
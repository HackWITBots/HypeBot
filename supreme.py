from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re as re


browser = webdriver.Chrome(executable_path='/Users/ryangould/PycharmProjects/HypeBot1/chromedriver')
browser.set_window_size(900,900)
browser.set_window_position(0,0)
sleep(1)
browser.get("https://www.supremenewyork.com/shop")
#browser.find_element_by_class_name("shop_link").click()

#shop = browser.find_elements_by_xpath('//*[@id="shop-scroller"]')

elems = browser.find_elements_by_xpath("//a[@href]")
elems1 = elems[3:46]
for elem in elems1:
    print(elem.get_attribute("href"))

sleep(1)

browser.close()

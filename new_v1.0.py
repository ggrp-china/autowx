import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def load(x,name,password):
    x.find_element_by_xpath("//*[@id='username']").click()
    x.find_element_by_xpath("//*[@id='username']").send_keys(name)
    x.find_element_by_xpath("//*[@id='password']").click()
    x.find_element_by_xpath("//*[@id='password']").send_keys(password)
    x.find_element_by_name("submit").click()


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://ehome.hrbeu.edu.cn/")

load(driver,"2018065117","11134212")
time.sleep(10)
driver.find_element_by_link_text("办事中心").click()
time.sleep(10)
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_link_text("平安行动").click()
time.sleep(10)
driver.switch_to.window(driver.window_handles[-1])
load(driver,"2018065117","11134212")
time.sleep(10)
driver.find_element_by_id("V1_CTRL82").click()
driver.find_element_by_class_name("command_button_content").click()
driver.find_element_by_class_name("default").click()
driver.find_element_by_class_name("default").click()



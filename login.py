#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

usernameStr = 'zengxiangrui'
passwordStr = 'Zeng5215210'
locationStr = '飯田橋・九段下/Iidabashi・Kudanshita'
areaStr = 'A1-12.北の丸スクエア'

browser = webdriver.Chrome('/home/zeng/Develop/WorkSpace/python/cycle/chromedriver')
browser.get(('https://tcc.docomo-cycle.jp/cycle/TYO/cs_web_main.php?AreaID=1'))

# fill in username and hit the next button

username = browser.find_element_by_name('MemberID')
username.send_keys(usernameStr)

password = browser.find_element_by_name('Password')
password.send_keys(passwordStr)

password.submit()

# wait for transition then continue to fill items

while True:
  portSelect = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Choose from port")))
  portSelect.click()

  select = Select(browser.find_element_by_id('Location'))
  select.select_by_value(locationStr)

  port = browser.find_element_by_partial_link_text(areaStr)
  port.click()

  list = browser.find_elements(By.XPATH, '//div[@class="cycle_list_btn"]/a')

  if len(list):
    list[1].click()
    break
  else:
    print 'Not available, try again in 30s'
    sleep(30)
    goback = browser.find_element(By.XPATH,'//input[@type="submit"]')
    goback.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver import ActionChains as A

import pyautogui as P
import time


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL1=r"https://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
URL2=r"https://crossbrowsertesting.github.io/drag-and-drop"
headling_css_locator=".post-body>div:nth-child(1)>div:nth-child(1)>form:nth-child(1)>h3:nth-child(1)"
distance_id_locator="distance"
draggable_id_locator="draggable"
droppable_id_locator="droppable"
wait_time_out=15
driver=webdriver.Chrome(executable_path=exec_path)
wait_variable=W(driver, wait_time_out)
driver.get(URL1)
headling_element=wait_variable.until(E.presence_of_element_located((By.CSS_SELECTOR,headling_css_locator)))
distance_element=wait_variable.until(E.presence_of_element_located((By.ID,distance_id_locator)))
a=A(driver)
a.double_click(headling_element)
a.move_to_element_with_offset(distance_element,0,0)
a.click_and_hold(distance_element)
a.release()
a.send_keys("1000")
a.perform()

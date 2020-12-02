from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver import ActionChains as A
from selenium.webdriver.common.keys import Keys as K
import pyautogui as P
import time


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
#URL2=r"https://crossbrowsertesting.github.io/drag-and-drop"
#headling_css_locator=".post-body>div:nth-child(1)>div:nth-child(1)>form:nth-child(1)>h3:nth-child(1)"
distance_id_locator="distance"
wait_time_out=15
driver=webdriver.Chrome(executable_path=exec_path)
wait_variable=W(driver, wait_time_out)
driver.get(URL)
distance_element=wait_variable.until(E.presence_of_element_located((By.ID,distance_id_locator)))
distance_element.send_keys("")
P.write("123456.78")
P.press("backspace",3)
P.hotkey("ctrl","a")
P.hotkey("ctrl","c")
P.sleep(1)
P.press("tab")
P.hotkey("ctrl","v")

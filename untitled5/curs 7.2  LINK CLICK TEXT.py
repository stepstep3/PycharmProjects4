from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://indership.blogspot.com"

wait_time_out=15
driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
wait_variable=W(driver, wait_time_out)
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT,"Selenium Python Tutorials"))).click()
driver.back()
wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Selenium Python"))).click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import Select
import time


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert"

driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)

frames=driver.find_elements_by_tag_name("iFrame")
print("there are", len(frames),"frames on this page")

for f in frames:
    print("frame id", f.get_attribute('id'),"Frame name", f.get_attribute('name'))
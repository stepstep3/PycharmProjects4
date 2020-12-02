from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://indership.blogspot.com"
frame_id_locator="iframeResult"
button_css_locator="body>button:nth-child(2)"
wait_time_out=15

driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
wait_variable=W(driver, wait_time_out)
links=wait_variable.until(E.visibility_of_any_elements_located((By.TAG_NAME,"a")))
print("number of links is ", len(links))
for link in links:
    print(link.text)
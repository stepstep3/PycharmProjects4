from selenium import webdriver
from selenium.webdriver.common.by import By
import time
exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://www.wikipedia.org"
english_link_locator="js-link-box-en"
search_locator="searchInput"
search_text="Software"

driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
driver.maximize_window()
english_link_element=driver.find_element(By.ID, english_link_locator)
english_link_element.click()
input_box_element=driver.find_element(By.ID, search_locator)
input_box_element.send_keys(search_text)
input_box_element.submit()
time.wait(100)
driver.quit()
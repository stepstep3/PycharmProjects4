from selenium import webdriver
from selenium.webdriver.common.by import By
import time
exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (3)\chromedriver.exe"
URL=r"https://www.wikipedia.org"
#english_link_locator="js-link-box-en"
language_locators=["js-link-box-en","js-link-box-ru","js-link-box-de"]
search_locator="searchInput"
search_text="Software"

driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
driver.maximize_window()
for i in range(len(language_locators)):
    language_link=driver.find_element(By.ID, language_locators[i])
    language_link.click()
    time.sleep(2)
    input_box_element=driver.find_element(By.ID, search_locator)
    input_box_element.send_keys(search_text)
    input_box_element.submit()
    time.sleep(3)
    driver.back()
    driver.back()
    time.sleep(3)
time.sleep(10)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time

exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://inderpsingh.blogspot.com/2013/04/SeleniumWebDriverQuiz4.html"
wait_time_out=5
answer1_radio_id_locator="13"
answer1_name_locator="answer1"

driver=webdriver.Chrome(executable_path=exec_path)
wait=W(driver, wait_time_out)
driver.get(URL)
radio_element = wait.until(E.presence_of_element_located((By.ID, answer1_radio_id_locator)))
radio_element.click()
answer1_element = wait.until(E.presence_of_element_located((By.NAME, answer1_name_locator)))

if "Correct." in answer1_element.get_attribute("value"):
    print ("Test passed")
else:
    print ("Test not passed")

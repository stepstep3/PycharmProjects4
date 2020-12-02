from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert"
frame_id_locator="iframeResult"
button_css_locator="body>button:nth-child(2)"
wait_time_out=5

driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
wait_variable=W(driver, wait_time_out)

wait_variable.until(E.frame_to_be_available_and_switch_to_it(frame_id_locator))
wait_variable.until(E.presence_of_element_located((By.CSS_SELECTOR,button_css_locator))).click()
wait_variable.until(E.alert_is_present())
driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.default_content()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time

exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://inderpsingh.blogspot.com/2013/04/SeleniumWebDriverQuiz4.html"
wait_time_out=5
#answer1_radio_id_locator="1"
answer_name_locator="answer"
score_id_locator="score"

driver=webdriver.Chrome(executable_path=exec_path)
wait=W(driver, wait_time_out)
driver.get(URL)
for q in range(1,7):
    for a in range(1,5):
      radio_element = wait.until(E.presence_of_element_located((By.ID, str(q)+str(a))))
      radio_element.click()
      time.sleep(1)
      answer_element = wait.until(E.visibility_of_element_located((By.NAME, answer_name_locator+str(q))))
      if "Correct." in answer_element.get_attribute("value"):
        break

score_element=wait.until(E.visibility_of_element_located((By.ID, score_id_locator)))
if "6/6" in score_element.text:
    print("Test passed")
else:
    print("Test not passed")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
wait_time_out=15

def answered(d, question_number):
    wait_variable=W(d, wait_time_out)
    answer_element=wait_variable.until(E.presence_of_element_located((By.NAME, "answer"+str(question_number))))
    if "Correct." in answer_element.get_attribute("value"):
        return True
    else:
        return False


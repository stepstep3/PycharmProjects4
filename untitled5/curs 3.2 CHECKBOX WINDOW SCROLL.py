from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import cursCheckboxFunction as C


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://inderpsingh.blogspot.com/2013/01/HTMLCSSQuiz1.html"
wait_time_out=15
check_name_locator="option"
driver=webdriver.Chrome(executable_path=exec_path)
wait=W(driver, wait_time_out)
driver.get(URL)

i=0
while i<10:
    i +=1
    driver.execute_script("window.scrollBy(0,120)","")
    check_element_1 = wait.until(E.presence_of_element_located((By.NAME, check_name_locator+str(i)+"1")))
    check_element_2 = wait.until(E.presence_of_element_located((By.NAME, check_name_locator+str(i)+"2")))
    check_element_3 = wait.until(E.presence_of_element_located((By.NAME, check_name_locator+str(i)+"3")))
    check_element_1.click()
    check_element_2.click()
    check_element_3.click()
    if C.answered(driver, i): continue
    check_element_1.click()
    if C.answered(driver, i): continue
    check_element_1.click()
    check_element_2.click()
    if C.answered(driver, i): continue
    check_element_2.click()
    check_element_3.click()
    if C.answered(driver, i): continue
    check_element_2.click()
    if C.answered(driver, i): continue
    check_element_1.click()
    check_element_2.click()
    if C.answered(driver, i): continue
    check_element_2.click()
    check_element_3.click()





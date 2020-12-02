from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import Select
import time


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
distance_id_locator="distance"
distance=0
speed_id_locator="speed"
speed=45
time_id_locator="hours"
calculate_css_locator=".post-body>div:nth-child(1)>div:nth-child(1)>form:nth-child(1)>button:nth-child(20)"
result_id_locator="result"
wait_time_out=5

driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
wait_variable=W(driver, wait_time_out)
driver.execute_script("window.scrollBy(0,240)","")
distance_element=wait_variable.until(E.presence_of_element_located((By.ID,distance_id_locator)))
speed_element=wait_variable.until(E.presence_of_element_located((By.ID,speed_id_locator)))
time_element=Select(wait_variable.until(E.presence_of_element_located((By.ID,time_id_locator))))
calculate_element=wait_variable.until(E.presence_of_element_located((By.CSS_SELECTOR, calculate_css_locator)))
result_element=wait_variable.until(E.presence_of_element_located((By.ID,result_id_locator)))

for option in time_element.options:
    distance_element.clear()
    distance +=100
    distance_element.send_keys(distance)
    speed_element.clear()
    speed +=1
    speed_element.send_keys(speed)
    time_element.select_by_visible_text(option.text)
    calculate_element.click()
    time.sleep(1)
    expected_result=round(float(distance)/float(speed)/float(option.get_attribute("value")),4)
    if expected_result==int(expected_result):expected_result=int(expected_result)
    if str(expected_result) in result_element.text:
        print("Passed", str(expected_result),result_element.text)
    else:
        print("not passed", str(expected_result),result_element.text)
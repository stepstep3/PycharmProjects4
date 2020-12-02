from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import pyautogui as P
import time


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
distance_id_locator="distance"
speed_id_locator="speed"
wait_time_out=15
driver=webdriver.Chrome(executable_path=exec_path)
wait_variable=W(driver, wait_time_out)
driver.get(URL)
distance_element=wait_variable.until(E.presence_of_element_located((By.ID,distance_id_locator)))
distance_element.send_keys("1000")
speed_element=wait_variable.until(E.presence_of_element_located((By.ID,speed_id_locator)))
speed_element.send_keys("50")
#time.sleep(5)
#x,y=P.position()
#print("X is",str(x),"Y is")
P.moveTo(170,888,3)
P.rightClick()


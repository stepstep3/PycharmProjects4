from selenium import webdriver
import Cursutilities as U

exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://www.wikipedia.org/"

driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
U.screenshot(driver)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import cursCheckboxFunction as C


exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
URL=r"https://wikipedia.org"
languages=["en","ja","fr"]
driver=webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
print("Window handle of current window is", driver.current_window_handle)

for i in range(len(languages)):
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[i+1])
        language_URL=r"https://"+languages[i]+".wikipedia.org/"
        driver.get(language_URL)
        print(language_URL,driver.window_handles[i+1],driver.title,driver.current_url)

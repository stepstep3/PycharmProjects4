from selenium import webdriver
from Pages.curs121MainPage import MainPage
from Pages.curs121EnglishPage import EnglishPage
import Cursutilities as U

exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
driver=webdriver.Chrome(executable_path=exec_path)
base_URL="https://www.wikipedia.org"

def set_up():
    driver.get(base_URL)

def test_main_page():
    mp=MainPage(driver)
    mp.test_title()
    U.screenshot(driver)

def test_english_page():
    ep=EnglishPage(driver)
    ep.search_text()
    U.screenshot(driver)

set_up()
test_main_page()
test_english_page()



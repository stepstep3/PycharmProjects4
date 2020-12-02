import unittest
from selenium import webdriver
from Pages.MainPage import MainPage
from Pages.EnglishPage import EnglishPage


class WikipediaTestClass1(unittest.TestCase):
  exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (3)\chromedriver.exe"
  base_URL="https://www.wikipedia.org"


  def test_main_page(self):
    driver = webdriver.Chrome(executable_path=self.exec_path)
    driver.get(self.base_URL)
    mp=MainPage(driver)
    mp.test_title()


  def test_english_page(self):
    driver = webdriver.Chrome(executable_path=self.exec_path)
    driver.get(self.base_URL)
    mp = MainPage(driver)
    mp.click_english_link()
    ep=EnglishPage(driver)
    ep.search_text()

if __name__=="__main_":
    unittest.main()






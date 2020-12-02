import unittest
from selenium import webdriver
from untitled5.Pages.MainPage import MainPage
from untitled5.Pages.EnglishPage import EnglishPage
import Cursutilities as U

class WikipediaTestClass1(unittest.TestCase):
  exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
  base_URL="https://www.wikipedia.org"
  driver = webdriver.Chrome(executable_path=exec_path)

  @classmethod
  def setUp(self):
    print("This method runs before every test method")
    self.driver.get(self.base_URL)


  @classmethod
  def tearDown(self):
    print("This method runs after every test method")

  def test_main_page(self):
    mp=MainPage(self.driver)
    mp.test_title()

  def test_english_page(self):
    mp = MainPage(self.driver)
    mp.click_english_link()
    ep=EnglishPage(self.driver)
    ep.search_text()

if __name__=="__main_":
    unittest.main()




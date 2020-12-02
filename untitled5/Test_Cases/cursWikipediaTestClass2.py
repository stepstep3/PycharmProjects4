import unittest
from selenium import webdriver
from untitled5.Pages.MainPage import MainPage
from untitled5.Pages.EnglishPage import EnglishPage
import untitled5.Cursutilities as U

class WikipediaTestClass2(unittest.TestCase):
  run_all_test_cases=True
  exec_path=r"C:\Users\NASA7\Downloads\chromedriver_win32 (4)\chromedriver.exe"
  base_URL="https://www.wikipedia.org"



  #@unittest.skipIf(run_all_test_cases==False,"This is medium priority testcase")
  #able if nittest.SkipTest is disabled
  def test_main_page(self):
    driver = webdriver.Chrome(executable_path=self.exec_path)
    driver.get(self.base_URL)
    mp=MainPage(driver)
    mp.test_title()

  #@unittest.SkipTest
  #able if unittest.skipIf is disabled
  def test_english_page(self):
    driver = webdriver.Chrome(executable_path=self.exec_path)
    driver.get(self.base_URL)
    mp = MainPage(driver)
    mp.click_english_link()
    ep=EnglishPage(driver)
    ep.search_text()

if __name__=="__main_":
    unittest.main()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E



class EnglishPage():
    search_id_locator="searchInput"
    term="Software"
    wait_time_out = 5

    def __init__(self,drv):
        self.drv=drv
        self.wait_variable=W(self.drv, self.wait_time_out)

    def test_title(self):
        assert self.title in self.drv.title

    def search_text(self):
        input_box_element=self.wait_variable.until(E.presence_of_element_located((By.ID,self.search_id_locator)))
        input_box_element.send_keys(self.term)
        input_box_element.submit()
        self.wait_variable.until(E.title_contains(self.term))




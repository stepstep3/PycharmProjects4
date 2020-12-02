from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E


class MainPage():
    title="Wikipedia"
    english_partial_link_text="English"
    wait_time_out = 5

    def __init__(self,drv):
        self.drv=drv
        self.wait_variable=W(self.drv, self.wait_time_out)

    def test_title(self):
        assert self.title in self.drv.title

    def click_english_link(self):
        self.wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT,self.english_partial_link_text))).click()









from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

def practiceSelenium():

    # get url "https://www.seleniumeasy.com/test/"
    driver = webdriver.Chrome()
    driver.get("https://www.seleniumeasy.com/test/")

    # start practice
    elementStart = '//*[@id="btn_basic_example"]'
    btnStart = driver.find_element_by_xpath(elementStart)
    btnStart.click()

if __name__=="__main__":
    practiceSelenium()

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    driver.maximize_window()

def test_search():

    search = driver.find_element_by_css_selector("#search")
    search.send_keys("Muon roi ma sao con")

    button = driver.find_element_by_css_selector("#search-icon-legacy")
    button.click()

    title = driver.title
    assert title == "YouTube"

def test_close():
    time.sleep(5)
    driver.close()




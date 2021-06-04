from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def googleSearch():

    # create object driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com.vn/?client=safari&channel=iphone_bm")

    # textField Search
    txtSearch = "html > body > div > div:nth-of-type(3) > form > div > div > div > div > div:nth-of-type(2) > input"
    enter_txtSearch = driver.find_element_by_css_selector(txtSearch)
    enter_txtSearch.send_keys("Tháng năm", Keys.CLEAR)

    # button Search
    btnSearch = "html > body > div > div:nth-of-type(3) > form > div > div > div:nth-of-type(3) > center > input"
    play_btnSearch = driver.find_element_by_css_selector(btnSearch)
    play_btnSearch.click()

    # play music
    element = '//*[@id="wp-tabs-container"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]'
    playMusic = driver.find_element_by_xpath(element)
    playMusic.click()

    # close window
    time.sleep(3)
    driver.close()

if __name__=="__main__":
    googleSearch()


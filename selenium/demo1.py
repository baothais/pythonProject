from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def search1():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.find_element_by_xpath("//*[@id=\"email\"]").send_keys("0935284861")
    driver.find_element_by_xpath("//*[@id=\"pass\"]").send_keys("thaibao96")
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
    time.sleep(10)

def search2():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com.vn/?client=safari&channel=iphone_bm")
    driver.find_element_by_name("q").send_keys("Thai Bao dep trai", Keys.RETURN)
    time.sleep(1000)

def search3():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    driver.find_element_by_xpath("//*[@id=\"search\"]").send_keys("muon roi ma sao con", Keys.RETURN)
    driver.find_element_by_xpath("//*[@id=\"search-icon-legacy\"]").click()
    # driver.find_element_by_xpath("//*[@id=\"img\"]").click()
    time.sleep(1000)

if __name__=="__main__":
    search2()



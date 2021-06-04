from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# def framgia():
#     driver = webdriver.Chrome()
#     driver.get("https://edev.sun-asterisk.vn/#")
#     driver.find_element_by_xpath("//*[@id=\"user_email\"]").send_keys("admin.wsm@framgia.com.edev.test")
#     driver.find_element_by_xpath("//*[@id=\"user_password\"]").send_keys("123456")
#     driver.find_element_by_xpath("//*[@id=\"wsm-login-button\"]").click()

def search1():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    driver.find_element_by_xpath("//*[@id=\"search\"]").send_keys("Muộn rồi mà sao còn")
    driver.find_element_by_xpath("//*[@id=\"search-icon-legacy\"]").click()
    time.sleep(100)

# def search3():
#     driver = webdriver.Chrome()
#     driver.get("https://www.youtube.com/")
#     driver.find_element_by_xpath("//*[@id=\"search\"]").send_keys("muon roi ma sao con", Keys.RETURN)
#     driver.find_element_by_xpath("//*[@id=\"search-icon-legacy\"]").click()
#     # driver.find_element_by_xpath("//*[@id=\"img\"]").click()
#     time.sleep(1000)

if __name__=="__main__":
    search1()
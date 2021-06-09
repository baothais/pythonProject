from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def links():

    driver = webdriver.Chrome()

    url = "http://demo.guru99.com/test/newtours/"
    driver.get(url)

    elementLinks = "a"
    links = driver.find_elements(By.TAG_NAME, elementLinks)

    # print("Number of links present: {}".format(len(links))) # print how many links present in a page
    #
    # print(type(links))
    #
    # for link in links:
    #     print(link.text)

    elementSupport = "SUPPORT"
    clickSupport = driver.find_element(By.LINK_TEXT, elementSupport)
    clickSupport.click()

    elementRegister = "REG"
    clickRegister = driver.find_element(By.PARTIAL_LINK_TEXT, elementRegister)
    clickRegister.click()

    driver.close()

if __name__=="__main__":
    links()



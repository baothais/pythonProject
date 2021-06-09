import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def handle_frames_iframes():

    driver = webdriver.Chrome()

    url = "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html"
    driver.get(url)

    driver.switch_to.frame("packageListFrame")
    driver.find_element(By.LINK_TEXT, "org.openqa.selenium.concurrent").click()

    time.sleep(3)
    driver.close()

if __name__=="__main__":
    handle_frames_iframes()
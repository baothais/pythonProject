import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def handle_alert_popup():

    driver = webdriver.Chrome()

    url = "http://testautomationpractice.blogspot.com/"
    driver.get(url)

    elementAlert = "//button[contains(text(),'Click Me')]"
    btnAlert = driver.find_element(By.XPATH, elementAlert)
    btnAlert.click()

    # alert = driver.switch_to.alert
    # alert.accept()    # close alert window using OK button

    alert = driver.switch_to.alert
    time.sleep(3)
    alert.dismiss()     # close alert window using Cancle button

    time.sleep(3)
    driver.close()
if __name__=="__main__":
    handle_alert_popup()


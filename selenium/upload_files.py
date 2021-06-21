import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def upload_files():

    driver = webdriver.Chrome()

    driver.implicitly_wait(5)

    url = "http://testautomationpractice.blogspot.com/"
    driver.get(url)

    driver.switch_to.frame(0)

    elementFiles = '//*[@id="RESULT_FileUpload-10"]'
    inputFiles = driver.find_element(By.XPATH, elementFiles)
    inputFiles.send_keys("/Users/bao/Desktop/Thai-Bao-CV-Automation_Tester.pdf")

    time.sleep(5)
    driver.close()

if __name__=="__main__":
    upload_files()

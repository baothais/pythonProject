import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def practice_selenium():

    driver = webdriver.Chrome()

    # get url "https://tiki.vn"
    url = "https://tiki.vn"
    driver.get(url)

    elementCancle = "onesignal-slidedown-cancel-button"
    """away 1: click on button"""
    # btnCancle = driver.find_element(By.ID, elementCancle)
    # btnCancle.click()
    """away 2: click on button using Explicit wait"""
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.ID, elementCancle)))


    # links = driver.find_elements(By.TAG_NAME, "a")
    #
    # for link in links:
    #     print(link.text)

    clickTicketbox = driver.find_element(By.LINK_TEXT, "Ticketbox")
    clickTicketbox.click()

    time.sleep(3)
    driver.close()

if __name__=="__main__":
    practice_selenium()
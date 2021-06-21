from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def handle_windows():

    driver = webdriver.Chrome()

    url = "http://demo.automationtesting.in/Windows.html"
    driver.get(url)

    elementClick = '//*[@id="Tabbed"]/a/button'
    btnClick = driver.find_element(By.XPATH, elementClick)
    btnClick.click()

    # print(driver.current_window_handle)     # window parent

    handles = driver.window_handles
    # print(handles)

    for handle in handles:
        driver.switch_to.window(handle)
        title = driver.title
        print(title)
        if title == "Frames & windows":
            driver.close()

    driver.close()

if __name__=="__main__":
    handle_windows()
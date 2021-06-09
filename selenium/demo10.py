from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_url():

    driver = webdriver.Chrome("/Users/bao/Downloads/chromedriver 4")
    driver.get("https://mail.google.com/mail/u/0/")
    print(driver.title)

if __name__=="__main__":
    get_url()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def navigation_command():

    driver = webdriver.Chrome(executable_path="/Users/bao/Downloads/chromedriver")

    # get url "https://www.google.com.vn/?client=safari&channel=iphone_bm"
    url1 = "https://www.google.com.vn/?client=safari&channel=iphone_bm"
    driver.get(url1)
    print(driver.title)
    time.sleep(3)

    # get url "https://mp3.zing.vn/"
    url2 = "https://mp3.zing.vn/"
    driver.get(url2)
    print(driver.title)
    time.sleep(3)


    driver.back()
    print(driver.title)
    time.sleep(3)

    driver.forward()
    print(driver.title)
    time.sleep(3)

    # driver.close()

if __name__=="__main__":
    navigation_command()
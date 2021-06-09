from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def input_box():

    driver = webdriver.Chrome()

    # wait
    driver.implicitly_wait(5)

    # get url
    url = "https://www.facebook.com/"
    driver.get(url)

    # input username
    elementUsername = "email"
    inputUsername = driver.find_element(By.ID, elementUsername)
    inputUsername.send_keys("hello")

    # status input box
    print("Displayed or not: {}".format(inputUsername.is_displayed()))
    print("Enabled or not: {}".format(inputUsername.is_enabled()))

    driver.close()

if __name__=="__main__":
    input_box()
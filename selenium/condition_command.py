from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def condition_command():

    driver = webdriver.Chrome(executable_path="/Users/bao/Downloads/chromedriver")

    # get url "https://careers.who.int/careersection/iam/accessmanagement/login.jsf?redirectionURI=https%3A%2F%2Fcareers.who.int%2Fcareersection%2Fex%2Fjobsearch.ftl%3Fftlcompclass%3DLoginComponent&TARGET=https%3A%2F%2Fcareers.who.int%2Fcareersection%2Fex%2Fjobsearch.ftl%3Fftlcompclass%3DLoginComponent"
    url = "https://careers.who.int/careersection/iam/accessmanagement/login.jsf?redirectionURI=https%3A%2F%2Fcareers.who.int%2Fcareersection%2Fex%2Fjobsearch.ftl%3Fftlcompclass%3DLoginComponent&TARGET=https%3A%2F%2Fcareers.who.int%2Fcareersection%2Fex%2Fjobsearch.ftl%3Fftlcompclass%3DLoginComponent"
    driver.get(url)
    print(driver.title)

    # input username
    elementUsername = "//input[@id='dialogTemplate-dialogForm-login-name1']"
    inputUsername = driver.find_element_by_xpath(elementUsername)

    print(inputUsername.is_displayed())
    print(inputUsername.is_enabled())

    # input password
    elementPassword = "//input[@id='dialogTemplate-dialogForm-login-password']"
    inputPassword = driver.find_element_by_xpath(elementPassword)


    print(inputPassword.is_enabled())
    print(inputPassword.is_displayed())

    # click on login button
    elementLogin = "//input[@id='dialogTemplate-dialogForm-login-defaultCmd']"
    btnLogin = driver.find_element_by_xpath(elementLogin)

    print(btnLogin.is_enabled())
    print(btnLogin.is_displayed())

    # login account
    inputUsername.send_keys("Hello World", Keys.CLEAR)
    inputPassword.send_keys("Hello World", Keys.CLEAR)
    btnLogin.click()

if __name__=="__main__":
    condition_command()





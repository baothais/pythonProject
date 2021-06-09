from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def implicit_wait():

    # create driver
    driver = webdriver.Chrome()

    # get url
    url = "https://mat.aima.in/may21/login"
    driver.get(url)

    # implicit wait
    driver.implicitly_wait(10, )

    # input email
    elementEmail = "//input[@id='login-email']"
    inputEmail = driver.find_element_by_xpath(elementEmail)
    inputEmail.send_keys("thaibao14h5@gmail.com", Keys.CLEAR)

    # input password
    elementPwd = "//input[@id='login-password']"
    inputPwd = driver.find_element_by_xpath(elementPwd)
    inputPwd.send_keys("imthaibao1996", Keys.CLEAR)

    # select date
    elementDate = "//select[@id='login-date']"
    selectDate = driver.find_element_by_xpath(elementDate)
    selectDate.send_keys("1", Keys.CLEAR)

    # select month
    elementMonth = "//select[@id='login-month']"
    selectMonth = driver.find_element_by_xpath(elementMonth)
    selectMonth.send_keys("n", Keys.CLEAR)

    # select year
    elementYear = "//select[@id='login-year']"
    selectYear = driver.find_element_by_xpath(elementYear)
    selectYear.send_keys("1", Keys.CLEAR)

    # click on login button
    elementLogin = "//input[@id='login-submit']"
    btnLogin = driver.find_element_by_xpath(elementLogin)
    try:
        btnLogin.click()
    except Exception as e:
        print("Has a wrong: {}".format(e))


    # close driver
    driver.close()

if __name__=="__main__":
    implicit_wait()
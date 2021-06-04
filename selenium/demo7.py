from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def WSM():

    # create object driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # get link "https://edev.sun-asterisk.vn" with basic auth "wsm:dangnhap_wsm"
        driver.get("https://wsm:dangnhap_wsm@edev.sun-asterisk.vn/")
    except Exception as e:
        print("Has a wrong: {}".format(e))

    # click login button
    elementBtnLogin = "body > div.wsm-index > div.slide-wsm-content.display-none > a"
    play_btnLogin = driver.find_element_by_css_selector(elementBtnLogin)
    play_btnLogin.click()

    # enter username
    elementUsername = "#user_email"
    enterUsername = driver.find_element_by_css_selector(elementUsername)
    enterUsername.send_keys("admin.wsm@framgia.com.edev.test")

    # enter password
    elementPassword = "#user_password"
    enterPassword = driver.find_element_by_css_selector(elementPassword)
    enterPassword.send_keys("123456")

    # click OK button
    elementBtnOK = "#wsm-login-button"
    play_btnOK = driver.find_element_by_css_selector(elementBtnOK)
    play_btnOK.click()

    # time.sleep(5)

if __name__=="__main__":
    WSM()
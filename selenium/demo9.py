from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def practiseSelenium():

    # handle notification facebook
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    # input username
    elementUsername = "#email"
    inputUsername = driver.find_element_by_css_selector(elementUsername)
    inputUsername.send_keys("0935284861", Keys.CLEAR)

    # input password
    elementPassword = "#pass"
    inputPassword = driver.find_element_by_css_selector(elementPassword)
    inputPassword.send_keys("thaibao96", Keys.CLEAR)

    # click on login button
    elementLogin = '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'
    btnLogin = driver.find_element_by_xpath(elementLogin)
    btnLogin.click()

    # # click on search button
    # elementSearch = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/span/div/div[2]/div/div[2]/div/div/div/span[2]/div/div"
    # btnSearch = driver.find_element_by_xpath(elementSearch)
    # btnSearch.click()

    # # search people to receive messages
    # # elementSearchPeople = "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/label/input"
    # elementSearchPeople = "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]"
    # inputSearchPeople = driver.find_element_by_xpath(elementSearchPeople)
    # inputSearchPeople.send_keys("Mai Thanh Phương", Keys.CLEAR)

    # click on people
    elementClick = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div/ul/div/li[1]/div/div/div/a/div[1]/div[1]/div/svg/g/image"
    btnClick = driver.find_element_by_xpath(elementClick)
    btnClick.click()

    # # open messenger
    # openMessenger = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a/div[1]/div[1]/img'
    # btnMessenger = driver.find_element_by_xpath(openMessenger)
    # btnMessenger.click()

    # # choose people to receive messages
    # elementChoose = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/a/div[1]/div[1]/div/svg/g/image"
    # btnChoose = driver.find_element_by_xpath(elementChoose)
    # btnChoose.click()

    # input message
    elemenInbox = '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div'
    inputMessage = driver.find_element_by_xpath(elemenInbox)
    inputMessage.send_keys("Hello Ku", Keys.RETURN)

    # # send message
    # elementSend = "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div/svg"
    # btnSend = driver.find_element_by_xpath(elementSend)
    # btnSend.click()

if __name__=="__main__":
    practiseSelenium()

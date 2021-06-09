import time

from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def explicit_waits():

    # create driver
    driver = webdriver.Chrome(executable_path="/Users/bao/Downloads/chromedriver")

    # wait
    driver.implicitly_wait(5)

    # get url "https://www.facebook.com/campaign/landing.php?&campaign_id=1661697988&extra_1=s%7Cc%7C515923224890%7Ce%7Cfacebook%7C&placement=&creative=515923224890&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D1661697988%26adgroupid%3D65157402478%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-541132862%26loc_physical_ms%3D9074104%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIndDL2bOD8QIVBlRgCh1mjgSvEAAYASAAEgL4q_D_BwE"
    url = "https://www.facebook.com/campaign/landing.php?&campaign_id=1661697988&extra_1=s%7Cc%7C515923224890%7Ce%7Cfacebook%7C&placement=&creative=515923224890&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D1661697988%26adgroupid%3D65157402478%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-541132862%26loc_physical_ms%3D9074104%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIndDL2bOD8QIVBlRgCh1mjgSvEAAYASAAEgL4q_D_BwE"
    driver.get(url)

    # click on royal_login_button
    elementRoyal = "menu_login_show_link"
    btnRoyal = driver.find_element_by_id(elementRoyal)
    btnRoyal.click()

    # element username
    elementUsername = "email"
    inputUsername = driver.find_element_by_id(elementUsername)
    inputUsername.send_keys("0935284861")

    wait = WebDriverWait(driver, 10)

    # element password
    elementPwd = "pass"
    inputPwd = driver.find_element_by_id(elementPwd)
    inputPwd.send_keys("thaibao96")

    # click on login button
    elementLogin = "loginbutton"
    btnLogin = driver.find_element_by_id(elementLogin)
    btnLogin.click()

    # close browser
    time.sleep(3)
    driver.close()

if __name__=="__main__":
    explicit_waits()


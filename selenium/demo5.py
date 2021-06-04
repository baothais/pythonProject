from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def loginAdmin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.phptravels.net/admin")
    driver.find_element_by_xpath('/html/body/div[2]/form[1]/div[1]/label[1]/input').send_keys("admin@phptravels.com")
    driver.find_element_by_xpath('/html/body/div[2]/form[1]/div[1]/label[2]/input').send_keys("demoadmin")
    driver.find_element_by_xpath('/html/body/div[2]/form[1]/button').click()
    # try:
    #     text = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/p').text
    # except:
    #     driver.close()
    #     assert False, "Test Failed"
    # else:
    time.sleep(5)
    driver.close()

def loginUser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.phptravels.net/home")
    driver.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div/div[2]/div/ul/li[3]/div/a").click()
    driver.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div/div[2]/div/ul/li[3]/div/div/div/a[1]").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div[1]/div[2]/form/div[3]/div[1]/label").send_keys("user@phptravels.com")
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div[1]/div[2]/form/div[3]/div[2]/label").send_keys("demouser")
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div[1]/div[2]/form/button").click()
    title = driver.title
    time.sleep(5)
    driver.close()

def loginSupplier():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.phptravels.net/supplier")
    txt = driver.current_url
    print(txt)
    # driver.save_screenshot("selenium/img/image.png")
    driver.find_element_by_xpath('/html/body/div[2]/form[1]/div[1]/label[1]/input').send_keys("supplier@phptravels.com")
    driver.find_element_by_xpath('/html/body/div[2]/form[1]/div[1]/label[2]/input').send_keys("demosupplier")
    driver.find_element_by_xpath('/html/body/div[2]/form[1]/button').click()
    try:
        title = driver.title
    except:
        assert title == "Dashboard"
    time.sleep(3)
    print(driver.title)
    driver.close()

if __name__=="__main__":
    # loginAdmin()
    # loginUser()
    loginSupplier()
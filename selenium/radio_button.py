import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def radio_button():

    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    url = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
    driver.get(url)

    # status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()
    # print(status)

    # driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[1]/td/label").click()
    #
    # time.sleep(5)
    # status1 = driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[1]/td/label").is_selected()
    # print(status1)

    # driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[2]/td/label").click()
    # status2 = driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[2]/td/label").is_selected()
    # print(status2)

    elementCheckbox = "//*[@id='q15']/table/tbody/tr[1]/td/label"
    clickCheckbox = driver.find_element(By.XPATH, elementCheckbox)
    clickCheckbox.click()

    status = clickCheckbox.is_selected()
    print(status)
    

    time.sleep(3)
    driver.close()

if __name__=="__main__":
    radio_button()
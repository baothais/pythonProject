from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.academia.edu/37960984/AI_Tr%C3%AD_tu%E1%BB%87_nh%C3%A2n_t%E1%BA%A1o_Thu%E1%BA%ADt_to%C3%A1n_A_N%E1%BB%99i_dung")

links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT, "Download Free PDF").click()


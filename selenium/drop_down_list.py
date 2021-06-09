import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def drop_down_list():

    driver = webdriver.Chrome()

    url = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
    driver.get(url)

    elementContact = "RESULT_RadioButton-9"
    selectContact = driver.find_element(By.ID, elementContact)

    drop = Select(selectContact)

    drop.select_by_visible_text("Morning")  # Morning

    # drop.select_by_index(2) # Evening

    # drop.select_by_value("Radio-1") # Afternoon
    print(len(drop.options))

    all_options = drop.options

    print(type(all_options))

    for option in all_options:
        print(option.text)

    driver.close()

if __name__=="__main__":
    drop_down_list()
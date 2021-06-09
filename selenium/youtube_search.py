from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def youtube_search():

    # create object driver
    driver = webdriver.Chrome(executable_path="/Users/bao/Downloads/chromedriver 4")

    # get "https://www.youtube.com/"
    url = "https://www.youtube.com/"
    driver.get(url)

    # # input keyword
    # element_input = "//input[@id='search']"
    # input_keyword = driver.find_element_by_xpath(element_input)
    # input_keyword.send_keys("Muon roi ma sao con", Keys.CLEAR)
    #
    # # click on search button
    # element_search  = "//button[@id='search-icon-legacy']"
    # play_btn_search = driver.find_element_by_xpath(element_search)
    # play_btn_search.click()

    # print title
    print(driver.title)
    print(driver.current_url)
    # print(driver.page_source)

    # close driver
    driver.close()

if __name__=="__main__":
    youtube_search()


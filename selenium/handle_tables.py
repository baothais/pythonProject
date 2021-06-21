from selenium import webdriver
from selenium.webdriver.common.by import By

def handle_tables():

    driver = webdriver.Chrome()

    url = "https://www.w3schools.com/html/html_tables.asp"
    driver.get(url)

    elementRow = "/html[1]/body[1]/div[7]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr"
    rows = len(driver.find_elements(By.XPATH, elementRow))      # count numbers of rows
    print(rows)

    elementCol = "/html[1]/body[1]/div[7]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/th"
    cols = len(driver.find_elements(By.XPATH, elementCol))
    print(cols)

    print("Company", "Contact", "Country", sep=" ")
    for row in range(2, rows+1):
        for col in range(1, cols+1):
            value = driver.find_element(By.XPATH, f"/html[1]/body[1]/div[7]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[{row}]/td[{col}]")
            print(value.text, end=" ")
        print()

    driver.close()

if __name__=="__main__":
    handle_tables()
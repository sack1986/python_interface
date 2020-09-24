from selenium import webdriver


def browser():
    #driver=webdriver.Firefox()
    #driver = webdriver.Chrome()
    driver=webdriver.Chrome()
    driver.maximize_window()
    return driver




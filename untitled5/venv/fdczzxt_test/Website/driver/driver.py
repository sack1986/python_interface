from selenium import webdriver


def browser():
    #driver=webdriver.Firefox()
    #driver = webdriver.Chrome()
    driver=webdriver.Ie()
    return driver



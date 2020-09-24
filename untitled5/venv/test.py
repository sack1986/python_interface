
from selenium import webdriver

def cs():
    driver=webdriver.Ie()
    driver.get("https://www.baidu.com")
    baidu=driver.find_element_by_id("kw")
    baidu.send_keys("ceshi")
    baidu.submit()


if __name__ == "__main__":
    cs()
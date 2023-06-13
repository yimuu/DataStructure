from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://www.cuishuai.cc/game/')


def main():
    sleep(0.5)
    print(driver)
    start = driver.find_element(by="css selector", value="#index > div:nth-child(3) > button")
    start.click()
    while True:
        colors = driver.find_elements(by="css selector", value="#box > span")
        styles = [i.get_attribute('style') for i in colors]
        ans = colors[styles.index(min(styles, key=styles.count))]
        ans.click()
        sleep(0.5)


if __name__ == '__main__':
    main()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def set_chrome_driver():
    chrome_options = Options()
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                              options = chrome_options)
    return driver

if __name__ == "__main__":
    driver = set_chrome_driver()
    driver.get('https://www.youthcenter.go.kr')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pc_gnb"]/ul/li[1]/a/span').click()
    driver.find_element(By.XPATH, '//*[@id="srchFrm"]/div[2]/div[1]/div[2]/div[2]/ul/li[3]/span/button').click()
    driver.find_element(By.XPATH, '//*[@id="srchFrm"]/div[2]/div[1]/div[5]/div[2]/span/label').click()
    driver.find_element(By.XPATH, '//*[@id="srchFrm"]/div[2]/div[2]/a[2]').click()
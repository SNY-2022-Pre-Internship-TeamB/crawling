from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        )
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                              options = chrome_options)
        self.driver.implicitly_wait(5)

    def __call__(self):
        return self.driver

    def get_url(self, url):
        self.driver.get(url)

    def get_html(self):
        return self.driver.page_source

    def find_xpath_element(self, xpath):
        return WebDriverWait(self.driver, 5, poll_frequency = 1).until(
            EC.presence_of_element_located((By.XPATH, xpath)),
            message = 'XPATH element not found'
        )

    def find_css_selector_element(self, css_selector):
        return WebDriverWait(self.driver, 5, poll_frequency = 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)),
            message = 'CSS_SELECTOR element not found'
        )

    def find_css_selector_elements(self, css_selector):
        return WebDriverWait(self.driver, 5, poll_frequency = 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)),
            message = 'CSS_SELECTOR elements not found'
        )

    def execute_script(self, script):
        self.driver.execute_script(script)

    def execute_onclick(self, link):
        self.driver.execute_script("arguments[0].click();", link)

    def wait(self, time):
        self.driver.implicitly_wait(time)

    def exit(self):
        self.driver.close()
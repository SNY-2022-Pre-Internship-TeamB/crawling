from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Driver Class
class Driver:
    # 초기화
    # 차단 방지를 위한 User-Agent 설정
    # ChromeDriver를 사용자 버전에 맞추어 설치
    # 웹페이지 로딩을 암묵적으로 대기함
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        )
        chrome_options.add_argument('headless')
        chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                              options = chrome_options)
        self.driver.implicitly_wait(5)

    def __call__(self):
        return self.driver

    # Url 접속
    def get_url(self, url):
        self.driver.get(url)

    # Html 저장
    def get_html(self):
        return self.driver.page_source

    # XPath로 특정 요소를 찾음
    # 해당하는 요소의 로딩을 기다리고, 로딩 되지 않았다면 exception 발생시킴
    def find_xpath_element(self, xpath):
        return WebDriverWait(self.driver, 5, poll_frequency = 1).until(
            EC.presence_of_element_located((By.XPATH, xpath)),
            message = 'XPATH element not found'
        )

    # css selector로 특정 요소를 찾음
    # 해당하는 요소의 로딩을 기다리고, 로딩 되지 않았다면 exception 발생시킴
    def find_css_selector_element(self, css_selector):
        return WebDriverWait(self.driver, 5, poll_frequency = 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)),
            message = 'CSS_SELECTOR element not found'
        )

    # css selector로 다수의 요소를 찾음
    # 해당하는 요소의 로딩을 기다리고, 로딩 되지 않았다면 exception 발생시킴
    def find_css_selector_elements(self, css_selector):
        return WebDriverWait(self.driver, 5, poll_frequency = 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)),
            message = 'CSS_SELECTOR elements not found'
        )

    # 자바스크립트를 실행시킴
    def execute_script(self, script):
        self.driver.execute_script(script)

    # 자바스크립트의 Onclick 이벤트를 실행시킴
    def execute_onclick(self, link):
        self.driver.execute_script("arguments[0].click();", link)

    # Driver를 종료시킴
    def exit(self):
        self.driver.delete_all_cookies()
        self.driver.close()
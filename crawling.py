from driver import Driver
import time

youthCenter = 'https://www.youthcenter.go.kr'
policy_housing_finance = ['//*[@id="pc_gnb"]/ul/li[1]/a/span',
                          '//*[@id="srchFrm"]/div[2]/div[1]/div[2]/div[2]/ul/li[3]/span/button',
                          '//*[@id="srchFrm"]/div[2]/div[1]/div[5]/div[2]/span/label',
                          '//*[@id="srchFrm"]/div[2]/div[2]/a[2]']

if __name__ == "__main__":
    driver = Driver()

    driver.get_url(youthCenter)
    print("사이트 접속 성공")

    for order, xpath in enumerate(policy_housing_finance):
        driver.find_xpath_element(xpath).click()
    print("정책 선택 완료")

    policy_num = driver.find_xpath_element('//*[@id="srchFrm"]/div[4]/div[1]/div[1]/strong/span').text
    print('정책 갯수 : ', policy_num)

    link = driver.find_css_selector_element('#dtlLink_R2022010701021')
    driver.execute_onclick(link)
    time.sleep(10)

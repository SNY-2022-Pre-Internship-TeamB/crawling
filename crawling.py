from driver import Driver

if __name__ == "__main__":
    driver = Driver()
    driver.get_url('https://www.youthcenter.go.kr')
    driver.find_xpath_element('//*[@id="pc_gnb"]/ul/li[1]/a/span').click()
    driver.find_xpath_element('//*[@id="srchFrm"]/div[2]/div[1]/div[2]/div[2]/ul/li[3]/span/button').click()
    driver.find_xpath_element('//*[@id="srchFrm"]/div[2]/div[1]/div[5]/div[2]/span/label').click()
    driver.find_xpath_element('//*[@id="srchFrm"]/div[2]/div[2]/a[2]').click()
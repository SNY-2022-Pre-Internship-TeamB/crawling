from driver import Driver
from bs4 import BeautifulSoup
import math

def get_policy_num(driver):
    youthCenter = 'https://www.youthcenter.go.kr'
    policy_housing_finance = ['//*[@id="pc_gnb"]/ul/li[1]/a/span',
                              '//*[@id="srchFrm"]/div[2]/div[1]/div[2]/div[2]/ul/li[3]/span/button',
                              '//*[@id="srchFrm"]/div[2]/div[1]/div[5]/div[2]/span/label',
                              '//*[@id="srchFrm"]/div[2]/div[2]/a[2]']
    policy_numbers = []

    driver.get_url(youthCenter)
    print("사이트 접속 성공")

    for order, xpath in enumerate(policy_housing_finance):
        driver.find_xpath_element(xpath).click()
    print("정책 선택 완료")

    total_num = int(driver.find_xpath_element('//*[@id="srchFrm"]/div[4]/div[1]/div[1]/strong/span').text)
    total_page_num = math.ceil(total_num / 12)
    print('정책 갯수 : ', total_num, '페이지 수 : ', total_page_num)

    aTags = driver.find_css_selector_elements('#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li > a')
    for aTag in aTags:
        policy_number = str(aTag.get_attribute('id')[8:])
        policy_numbers.append(policy_number)

    print("{}개 정책의 정책번호 저장 완료".format(len(policy_numbers)))

    return policy_numbers

def inject_script(driver):
    script = """
    function f_Detail(key){
        $("#srchAge").val($("#srchAge").val().replace(/[^0-9]/gi,""));
        $("#bizId").val(key);
        var srchFrm = document.srchFrm;
        srchFrm.action = "/youngPlcyUnif/youngPlcyUnifDtl.do";
        srchFrm.submit();}
    """

    driver.execute_script(script)
    driver.execute_script("f_Detail('R2021021800114')")

def parsing_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

if __name__ == "__main__":
    print("크롤링 시작")
    driver = Driver()

    policy_numbers = get_policy_num(driver)
    driver.exit()
    #parsing_html(result)



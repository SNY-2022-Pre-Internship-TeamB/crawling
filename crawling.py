from driver import Driver
from bs4 import BeautifulSoup
import math
import time
def get_policy_num(driver):
    # 청년정책 통합검색 사이트의 URL과, 주거/금융 유형 세부검색을 위한 XPath
    youthCenter = 'https://www.youthcenter.go.kr'
    policy_housing_finance = ['//*[@id="pc_gnb"]/ul/li[1]/a/span',
                              '//*[@id="srchFrm"]/div[2]/div[1]/div[2]/div[2]/ul/li[3]/span/button',
                              '//*[@id="srchFrm"]/div[2]/div[1]/div[5]/div[2]/span/label',
                              '//*[@id="srchFrm"]/div[2]/div[2]/a[2]']

    count = 0
    policy_numbers = []

    # 청년정책 통합검색 사이트 접속
    driver.get_url(youthCenter)
    print("사이트 접속 성공")

    # 세부검색을 위해 지정된 버튼을 순차적으로 클릭
    for order, xpath in enumerate(policy_housing_finance):
        driver.find_xpath_element(xpath).click()
    print("정책 선택 완료")

    # 검색된 정책의 총 개수, 페이지 수를 저장
    total_num = int(driver.find_xpath_element('//*[@id="srchFrm"]/div[4]/div[1]/div[1]/strong/span').text)
    total_page_num = math.ceil(total_num / 12)
    print('정책 갯수 : ', total_num, '페이지 수 : ', total_page_num)

    # 페이지 수 만큼 순회
    for page in range(total_page_num):
        # 한 페이지에 보여지는 정책들의 정책번호를 받아서 저장
        aTags = driver.find_css_selector_elements(
            '#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li > a')
        for aTag in aTags:
            policy_number = str(aTag.get_attribute('id')[8:])
            policy_numbers.append(policy_number)

        # 다음 페이지로 이동
        count += 1
        driver.execute_script("fn_move({})".format(count + 1))

    print("{}개 정책의 정책번호 저장 완료".format(len(policy_numbers)))

    return policy_numbers

def get_policy_detail(driver, policy_numbers):
    html_list = []
    # 정책 번호를 이용하여 상세 페이지로 이동하는 자바스크립트
    # JS의 스코핑 룰 때문에 전역함수로 선언해주어야 함
    script = """
    window.f_Detail = function f_Detail(key){
        $("#srchAge").val($("#srchAge").val().replace(/[^0-9]/gi,""));
        $("#bizId").val(key);
        var srchFrm = document.srchFrm;
        srchFrm.action = "/youngPlcyUnif/youngPlcyUnifDtl.do";
        srchFrm.submit();}
    """

    # 저장된 정책번호를 순차적으로 돌면서, 상세 페이지를 보여주는 자바스크립트를 실행
    # 상세 페이지로 이동 한 뒤, 해당 페이지를 html로 저장
    for policy_number in policy_numbers:
        driver.execute_script(script)
        driver.execute_script("f_Detail('{}')".format(policy_number))
        html_list.append(driver.get_html())
    return html_list

def parse_html(html_list):
    for html in html_list:
        soup = BeautifulSoup(html, 'html.parser')

if __name__ == "__main__":
    # 초기화
    driver = Driver()
    print("크롤링 시작")

    # 정책 번호 받아오기
    policy_numbers = get_policy_num(driver)

    # 정책 번호에 해당하는 html 받아오기
    html_list = get_policy_detail(driver, policy_numbers)

    # 받아온 html을 파싱
    parse_html(html_list)

    # 종료
    driver.exit()



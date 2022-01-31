from crawler import *
from parser import *

if __name__ == "__main__":
    # 초기화
    html_list = []
    driver = Driver()
    print("크롤링 시작")

    # 정책 번호 받아오기
    policy_numbers = get_policy_num(driver)

    # 정책 번호에 해당하는 html 받아오기
    html_list = get_policy_detail(driver, policy_numbers, html_list)

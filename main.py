import multiprocessing as mp
import numpy as np
import parmap
from crawler import *
from parser import *
import csv
import os
import time

if __name__ == "__main__":
    results = []

    # 로그 제거
    os.environ['WDM_LOG_LEVEL'] = '0'

    # 정책 번호 받아오기
    print("크롤링 시작")
    policy_numbers = get_policy_num()

    # 멀티프로세싱
    # 공유 변수 설정
    manager = mp.Manager()
    html_list = manager.list()

    # 프로세스 개수 설정
    num_processes = 4

    # 정책 번호 나누기
    policy_numbers = np.array_split(policy_numbers, num_processes)
    policy_numbers = [x.tolist() for x in policy_numbers]

    # 정책 번호에 해당하는 html 받아오기
    print("정책 세부사항 크롤링 시작")
    parmap.map(get_policy_detail, policy_numbers, html_list,
               pm_pbar = True, pm_processes = num_processes)

    # 받아온 html 파싱
    print("파싱 시작")
    start_time = time.time()
    for html in html_list:
        results.append(parse_html(html))
    end_time = time.time()
    print("파싱 소요 시간 : {}".format(end_time - start_time))

    with open("result.csv", 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(results)

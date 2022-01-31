from bs4 import BeautifulSoup

# 파싱한 각 요소에서 context를 추출
def getText(soup_select):
    for index, element in enumerate(soup_select):
        return element.text.strip()

# 각 요소별로 추출
def parse_html(html):
    context_list = []
    text_list = []
    soup = BeautifulSoup(html, 'html.parser')

    # 정책 일반 정보
    # 정책 이름, 정책 번호, 정책 소개 순
    p1 = soup.select(
        '#content > h3.doc_tit02.green.plcy-mobile > div.plcy-left')
    p2 = soup.select(
        '#content > h3.doc_tit02.green.plcy-mobile > div.plcy-number > span:nth-child(3)')
    p3 = soup.select(
        '#content > div.ply-view-section.green > div.tit-box > h4')

    # 한 눈에 보는 정책 요약
    # 정책 유형, 지원 내용, 사업 운영 기간, 사업 신청 기간, 지원 규모 순
    s1 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(2) > ul > li:nth-child(1) > div.list_cont')
    s2 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(2) > ul > li:nth-child(2) > div.list_cont')
    s3 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(2) > ul > li:nth-child(3) > div.list_cont')
    s4 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(2) > ul > li:nth-child(4) > div.list_cont')
    s5 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(2) > ul > li:nth-child(5) > div.list_cont')

    # 신청 자격
    # 언령, 거주지 및 소득, 학력, 전공, 취업 상태, 특화 분야, 추가 단서 사항, 참여 제한 대상
    q1 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(4) > ul > li:nth-child(1) > div.list_cont')
    q2 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(4) > ul > li:nth-child(2) > div.list_cont')
    q3 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(4) > ul > li:nth-child(3) > div.list_cont')
    q4 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(4) > ul > li:nth-child(4) > div.list_cont')
    q5 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(4) > ul > li:nth-child(5) > div.list_cont')
    q6 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(4) > ul > li:nth-child(6) > div.list_cont')
    q7 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(4) > ul > li:nth-child(7) > div.list_cont')
    q8 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(4) > ul > li:nth-child(8) > div.list_cont')

    # 신청 방법
    # 신청 절차, 심사 및 발표, 신청 사이트, 제출 서류 순
    h1 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(6) > ul > li:nth-child(1) > div.list_cont')
    h2 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(6) > ul > li:nth-child(2) > div.list_cont')
    h3 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(6) > ul > li:nth-child(3) > div.list_cont')
    h4 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(6) > ul > li:nth-child(4) > div.list_cont')

    # 기타
    # 기타 유익 정보, 주관 기관, 운영 기관, 사업 관련 참고 사이트1, 사업 관련 참고 사이트2, 첨부파일, 관련 첨부파일 순
    e1 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(8) > ul > li:nth-child(1) > div.list_cont')
    e2 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(8) > ul > li:nth-child(2) > div.list_cont')
    e3 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(8) > ul > li:nth-child(3) > div.list_cont')
    e4 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(8) > ul > li:nth-child(4) > div.list_cont')
    e5 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(8) > ul > li:nth-child(5) > div.list_cont')
    e6 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(8) > ul > li:nth-child(6) > div.list_cont')
    e7 = soup.select(
        '#content > div.ply-view-section.green > div.view-txt > div:nth-child(8) > ul > li:nth-child(7) > div.list_cont')

    context_list.append(p1, p2, p3, s1, s2, s3, s4, s5, q1, q2, q3, q4, q5, q6, q7, q8,
                        h1, h2, h3, h4, e1, e2, e3, e4, e5, e6, e7)

    for i in range(len(context_list)):
        text = getText(context_list[i])
        text_list.append(text)

    return text_list

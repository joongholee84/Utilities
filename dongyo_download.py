# This downloads mp3 files from http://www.dongyo.or.kr/, which is 동요사이트.
# There are two menues, 동요듣기, 새노래 in 희망프로젝트.
# We can downloads free-open mp3 files from theses.
# This program make it automated.
# made on 2024.02.20

#--------- Test codes --------------------------------------------
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time

# def download_file(url):
#     ## 자동으로 설치하여 버전 관리
#     # driver = webdriver.Chrome(ChromeDriverManager().install())
    
#     ## Chrome 드라이버 직접 다운로드 및 경로 지정.
#     #driver_path = 'c:/Program Files/Google/chromedriver-win64/chromedriver.exe'  # 본인 컴퓨터에 맞는 드라이버 경로로 수정해주세요.
#     # cService = webdriver.ChromeService(executable_path=driver_path)
#     # driver = webdriver.Chrome(service = cService)
    
#     ## 최신 버전은 걍 알아서 함.
#     driver = webdriver.Chrome()
    
#     driver.implicitly_wait(3)

#     try:
#         # URL 열기
#         driver.get(url)

#         # 파일 다운로드를 위해 잠시 대기
#         time.sleep(5)  # 예시로 5초 대기 (필요에 따라 조정 가능)
#         print(driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table[1]/tbody/tr/td/table[4]/tbody/tr[1]/td/table/tbody/tr[1]/td[3]/a').text, "\n")

#     finally:
#         # 브라우저 종료
#         driver.quit()

# # 다운로드 받을 URL 지정
# url = 'http://www.dongyo.or.kr'

# # 파일 다운로드 함수 호출
# download_file(url)
#------------------------------------------------------------------

import requests
import re

def find_mp3(html_content):
    
    try:
        # 정규표현식을 사용하여 ".mp3"로 끝나는 링크를 찾습니다.
        pattern_name = r'_[^"]+.mp3 '
        pattern_path = r'\/data\/file[^"]+.mp3'
        mp3_name = str(re.findall(pattern_name, html_content)[0]).replace("_","",1).replace(" ","",1)
        mp3_path = str(re.findall(pattern_path, html_content)[0])
        mp3_path = 'http://www.dongyo.or.kr/_ver02/_bbs_iw2000' + mp3_path
        
        # print(mp3_name)
        # print(mp3_path)

        # ".mp3"로 끝나는 링크만 추출합니다.
        # mp3_links = [link[1] for link in mp3_links if link[1].lower().endswith('.mp3')]

        return {'name':mp3_name,'path':mp3_path}
    except Exception:
        print("mp3 not found")
        return 1

def get_html_content(url):
    # 웹페이지에 GET 요청 보내기
    response = requests.get(url)
    
    # 응답 확인
    if response.status_code == 200:
        response.encoding = 'EUC-KR'
        # HTML 내용 출력
        print("Page found")
        return response.text
    else:
        print(f"웹페이지 접속 실패: {response.status_code}")
        return 1
    
def download_mp3(url, save_path):
    # MP3 파일 다운로드
    response = requests.get(url, stream=True)
    
    # 응답 확인
    if response.status_code == 200:
        # 파일 저장
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"MP3 파일 다운로드 완료: {save_path}")
    else:
        print(f"MP3 파일 다운로드 실패: {url}")

mp3_info = {}
bo_tables = ['0301','0303'] # 희망프로젝트 내의 동요듣기, 새노래
for bo_table in bo_tables:
    for page_id in range(1,700):
        url = f"http://www.dongyo.or.kr/_ver02/_bbs_iw2000/?doc=bbs/board.php&bo_table={bo_table}&page=1&wr_id={page_id}&stext="  # 접속할 웹페이지의 URL로 대체해야 합니다.
        print(url)
        # HTML 내용을 가져와 출력하는 함수 호출

        html_content = get_html_content(url)
        if html_content != 1:
            mp3_info = find_mp3(str(html_content))
            print(f"mp3_info = {mp3_info}")
            if mp3_info != 1:

                # 다운로드할 MP3 파일의 URL
                name = mp3_info['name']
                path = mp3_info['path']

                # 저장할 경로와 파일명 설정
                save_path = f"C:\\Users\\joong\Downloads\\{bo_table}\\{name}"  # 저장할 MP3 파일의 경로와 파일명으로 대체해야 합니다.
                print(f"save_path = {save_path}")
                # MP3 파일 다운로드 함수 호출
                download_mp3(path, save_path)

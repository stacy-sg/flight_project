import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 경로 설정
chrome_driver_path = "C:/Users/tmfrl/OneDrive/바탕 화면/new_project/chromedriver.exe"
chrome_options = Options()
chrome_options.headless = True
#chrome_options.add_argument("--disable-gpu") #gpu를 이용한 가속 끄기
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# 네이버 항공권 사이트 열기
driver.get('https://flight.naver.com/')
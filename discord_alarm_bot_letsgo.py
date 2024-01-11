import requests 
import re
from bs4 import BeautifulSoup

res = requests.get("https://kloa.gg/merchant")
print("응답 코드 : ", res.status_code)

if res.status_code == requests.codes.ok :
    print("정상입니다.")
else :
    print("문제가 생겼습니다. [에러코드 ", res.status_codel, "]")

res.raise_for_status()
print("웹 스크래핑을 진행합니다.")

test_str = "text-[#EB9500] dark:text-[#FFC766] px-[4px] leaging-[22px] shrink-0"

p = re.compile('\([^)]+\)')
m = p.findall(test_str)
# 정규표현식으로 특수문자를 포함한 전설카드 클래스명을 추출 및 검색하려하는데 실패했다.
# 정규표현식으로 특수문자 추출하는 식을 다시 짜야될 것 같다.

soup = BeautifulSoup(res.text, "lxml")
print(soup.title.get_text())
print(soup.a["href"])
print((soup.find(attrs={"class" : "text-[#EB9500] dark:text-[#FFC766] px-[4px] leaging-[22px] shrink-0"})))
# "text-[#EB9500] dark:text-[#FFC766] px-[4px] leaging-[22px] shrink-0" - 바훈투르와 카마인의 공통점 : 전설카드의 클래스명으로 추정된다.
# 문제가 발생 : 찾고자하는 것은 전설카드의 클래스명인데 실행할때마다 'None' 이 뜬다. 전설카드 클래스명에 특수문자가 들어가는게 원인인 것 같은데 정규표현식이 원인인 것 같다.
# API
* 주소를 기반으로 정보를 가져올 수 있음

## Request의 의미
* Requests란 Python용 HTTP 라이브러리
* 특정 웹사이트에 HTTP 요청을 보내 HTML 문서를 받아올 수 있는 라이브러리
    * pip install requests 이거 설치 하라는데 내가 이거 설치 했었는지 기억이 안 남..
* requests.get(url)을 통해 보낸 요청을 res라는 변수에 저장한 것
* response.json() 은 딕셔너리 타입으로 바로 변환하는 것

</br>

## if __name__ == '__main__': 의 의미 - ??
* 현재 스크립트 파일이 실행되는 상태를 파악하기 위해
* 즉, 프로그램의 시작점일 때는 if __name__ == '__main__': 아래의 코드가 실행됩니다.
* __name__ 변수의 값이 '__main__'일 때만 실행

## import requests하는 방법

```python 
# 1. 직접 입력해서 보내기
# url에 보내고자 하는 데이터를 입력해서 전송한다.
URL = "http://google.com?user=comp&num=42"
response = requests.get(URL)
print("status code :", response.status_code)

# 2. dict 이용하기
param = { "user" : "comp", "num" : 42 }
response = requests.get(URL, params=param)
print("status code :", response.status_code)

#3. 예시
# https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
# &로 연결!!


```

## json으로 가져온 데이터는 딕셔너리의 형태로 저장
```python
 res = requests.get(url=url).json() 
print(res)
>>
{'status': '0000', 'data': {'opening_price': '22623000', 'closing_price': '23581000', 'min_price': '22623000', 'max_price': '23918000', 'units_traded': '2282.9089742', 'acc_trade_value': '53509528846.1489', 'prev_closing_price': '22623000', 'units_traded_24H': '3779.39228821', 'acc_trade_value_24H': '87598218501.3294', 'fluctate_24H': '783000', 'fluctate_rate_24H': '3.43', 'date': '1673587599253'}}

data = res["data"]
# 이중 딕셔너리로 data안에 opening_price, min_price 등 다양한 정보가 들어가있음
#접근하기 위해서는 인덱싱으로
# ex 종가에 접근
prev_closing_price = data["prev_closing_price"]
>> 22623000



```
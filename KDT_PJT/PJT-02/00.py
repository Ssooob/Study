import requests 

# 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
def get_btc_krw() :
    order_currency = "BTC" # 종류를 선택하는 것인가 봄
    payment_currency = "KRW" # 옵션
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"
    # 다음과 같이 모든 정보는 홈페이지 URL로 접근할 수 있음
    # 필요한 부분에 대하여 option으로 넣고 url 구성해 데이터를 가져옴

    res = requests.get(url=url).json() 
    # requests.get(url)을 통해 해당 페이지의 정보를 보내달라 요청한 것을 res라는 변수에 저장한 것
    print(res)
    data = res["data"]
    prev_closing_price = data["prev_closing_price"]
    #데이터들이 딕셔너리 형태로 있나봄
    # request가 말하는 바가 뭐지 
    return prev_closing_price

if __name__ == "__main__" :
    print(get_btc_krw())
    
    # 종가가 출력되는 것
'''
requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록
(Get Populations) 데이터를 요청합니다.

응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.
https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
# 
'''

import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    cnt = 0
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/movie/popular'
    params = { # 그 문서에서 필요한 params 정의
    'api_key': '',
    'language': 'ko-KR',
    'region': 'KR' 
    }
    response = requests.get(BASE_URL+PATH, params=params).json()
    print(len(response.get('results')))
    # 안쪽 데이터 형태를 보면 [0] page [1]result 로 되어있고
    # result 안에는 list가 있고 그 list 내에 딕셔너리로 정보가 있음
    # 이는, 각 리스트로 딕셔너리가 저장되어있다는 의미
    # 각 영화는 딕셔너리의 형태로 results의 list에 저장
    # result의 구조를 살펴봐야함
    # {"page"
    #  "results": [ { 
    #               "adults" : 
    #               "backdrop_path" : 
    #               "genre_ids" : ...},
    # 
    #               { "adults" : 
    #               "backdrop_path" : 
    #               "genre_ids" : ...}, 가 반복
    # }]}

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

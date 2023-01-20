import requests
from pprint import pprint


def vote_average_movies():
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/movie/popular'
    params = { # 그 문서에서 필요한 params 정의
    'api_key': '',
    'language': 'ko-KR',
    'region': 'KR' 
    }
    response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=&language=ko-KR&page=1').json()
    high_movies_vote_avg = []
    for i in range(len(response.get('results'))):
      if response.get('results')[i].get('vote_average') >=8 : 
        high_movies_vote_avg.append(i)
        print(response.get('results')[i])

  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',ㄴ
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """

# 나의 경우 장화신은 고양이
'''
{'adult': False, 'backdrop_path': '/r9PkFnRUIthgBp2JZZzD380MWZy.jpg', 'genre_ids': [16, 28, 12, 35, 10751, 14], 'id': 315162, 'original_language': 'en', 'original_title': 'Puss in Boots: The Last Wish', 'overview': "아홉 개의 목숨 중 단 하나의 목숨만 남은 장화신은 고양이.  마지막 남은 목숨을 지키기 위해 히 어로의 삶 대신 반려묘의 삶을 선택한 그에게 찾아온 마지막 기회, 바로 소원을 들어주는 소원별이 있는 곳을 알려주는 지도!  잃어버린 목숨을 되찾고 다시 히어로 가 되기를 꿈꾸는 장화신은 고양이는 뜻밖에 동료가 된 앙숙 파트너 '키티 말랑손', 그저 친구들과 함께라면 모든 게 행복한 강아지 '페로'와 함께 소원별을 찾기 위해 길을 떠난다.  그리고 소원별을 노리는 또 다른 빌런들과 마주치게 되는데…", 'popularity': 10102.273, 'poster_path': '/rKgvctIuPXyuqOzCQ16VGdnHxKx.jpg', 'release_date': '2022-12-21', 'title': '장화신은 고양이: 끝내주는 모험', 'video': False, 'vote_average': 8.6, 'vote_count': 1215}
'''
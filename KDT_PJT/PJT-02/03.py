import requests
from pprint import pprint


def ranking():
    pass
    # 여기에 코드를 작성합니다.
    response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=&language=ko-KR&page=1').json()
    movie_details = response.get('results', None)
    sort_value = sorted(movie_details,key = lambda x : x['vote_average'])
    sort_value5 = sort_value[:5]
    return sort_value5


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
# 내꺼
'''
[{'adult': False,
  'backdrop_path': '/mYQSbZdGX0JJb49NLO04UA0iFEU.jpg',
  'genre_ids': [28, 35, 80],
  'id': 1015963,
  'original_language': 'en',
  'original_title': 'High Heat',
  'overview': '',
  'popularity': 1158.65,
  'poster_path': '/mmD0NVdhiRiCu64YKem5GK5PSfy.jpg',
  'release_date': '2022-12-16',
  'title': 'High Heat',
  'video': False,
  'vote_average': 4.9,
  'vote_count': 21},
 {'adult': False,
  'backdrop_path': '/rodjjIJ8oh9nuBp86PhojcYHTEN.jpg',
  'genre_ids': [28, 53, 80, 18],
  'id': 740952,
  'original_language': 'en',
  'original_title': 'Savage Salvation',
  'overview': '마약 중독을 이겨내고 새로운 삶을 살길 원하는 ‘존’(잭 휴스턴)과 ‘루비’(윌라 피츠제럴드). 둘은 결혼을 '
              "약속하고 루비의 형부 ‘피터'(존 말코비치)는 존을 가족으로 따뜻하게 맞아준다. 과 거의 죄를 씻고 구원을 바라는 "
              '루비의 세례를 앞둔 날, 약물 과다 투여로 죽어 있는 루비를 발견한 존은 절망에 빠 지고 그녀를 죽음에 이르게 한 '
              '마약 공급책을 끝장내기 위해 복수에 나선다. 마을의 ‘마이크’ 보안관(로버트 드 니 로)은 존의 폭주를 막기 위해 '
              '뒤를 쫓는데...',
  'popularity': 1271.242,
  'poster_path': '/lvaksAQd82i4fJqr16664GcGUTf.jpg',
  'release_date': '2022-12-02',
  'title': '새비지 맨',
  'video': False,
  'vote_average': 5.5,
  'vote_count': 26},
 {'adult': False,
  'backdrop_path': '/5wDBVictj4wUYZ31gR5WzCM9dLD.jpg',
  'genre_ids': [16, 878, 12, 10751],
  'id': 877269,
  'original_language': 'en',
  'original_title': 'Strange World',
  'overview': '전설적인 탐험가 가문 클레이드 패밀리의 서처 클레이드는 아내 메리디언, 아들 이든과 함께 농장을 운영하며 평화로운 '
              '일상을 살고 있다. 어느 날, 대통령 칼리스토가 찾아와 위험에 빠진 아발로니아를 위해 도움을 요청하고 서처는 '
              '내키지 않지만 어쩔 수 없이 가족들과 모험에 나서게 된다. 모든 것이 살아 숨 쉬는 미지의 세계에 도착한 서처는 '
              '오래전 행방불명 되었던 아버지, 전설의 탐험가 예거 클레이드를 만나게 된다. 여전 히 엉뚱하고 탐험 의욕이 넘치는 '
              '아버지 예거와 평화로운 삶을 살고 싶은 서처, 그리고 서처와는 다른 삶을 꿈꾸는 아들 이든까지 서로 너무 다른 '
              '개성 강한 클레이드 패밀리는 누구도 본 적 없고, 가본 적 없는 신비롭고 경이로운  세계에서 무사히 집으로 돌아갈 '
              '수 있을까?',
  'popularity': 1211.203,
  'poster_path': '/7KT8E7CpEwxQUay5nROpY6mCK8F.jpg',
  'release_date': '2022-11-23',
  'title': '스트레인지 월드',
  'video': False,
  'vote_average': 6.5,
  'vote_count': 585},
 {'adult': False,
  'backdrop_path': '/53BC9F2tpZnsGno2cLhzvGprDYS.jpg',
  'genre_ids': [14, 28, 12],
  'id': 736526,
  'original_language': 'no',
  'original_title': 'Troll',
  'overview': '고대의 전설이 깨어났다! 아주 오랜 세월, 노르웨이의 산에 잠들어 있던 트롤. 녀석 이 세상을 파괴하기 전에 막아야 '
              '한다. 골칫덩어리 영웅들이 힘을 합쳐야 가능하지만.',
  'popularity': 1935.884,
  'poster_path': '/6MEYnNtvyctpshK0nIi6Kor9Av9.jpg',
  'release_date': '2022-12-01',
  'title': '트롤의 습격',
  'video': False,
  'vote_average': 6.7,
  'vote_count': 982},
 {'adult': False,
  'backdrop_path': '/edOt2jNyCbb8SQSvulD2sRRJhmA.jpg',
  'genre_ids': [28, 80, 53],
  'id': 873126,
  'original_language': 'it',
  'original_title': 'Il mio nome è vendetta',
  'overview': '과거의 적들이 아내와 아내의 오빠를 살해하자, 딸과 함께 밀라노로 도망친 전직 마 피아 집행자. 그곳에서 몸을 숨긴 '
              '채 복수를 계획한다.',
  'popularity': 1140.678,
  'poster_path': '/5LG3gldi20hLxBHmWlJtt92Y73k.jpg',
  'release_date': '2022-11-30',
  'title': '마이 네임 이즈 벤데타',
  'video': False,
  'vote_average': 6.7,
  'vote_count': 292}]

'''
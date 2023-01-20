import requests
from pprint import pprint



def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    params = { # 그 문서에서 필요한 params 정의
    'api_key': '',
    'language': 'ko-KR',
    'region': 'KR',
    'query' : str(title)
    }

    response = requests.get(BASE_URL+PATH, params=params).json().get('results', None)
    
    return response
    '''
    return len(response.get('results'))
    
    for i in range(len(response.get('results'))):
      if response.get('results')[i].get('original_title') == title : 
        movie_id = response.get('results')[i].get('id')
        return movie_id

      elif response.get('results')[i].get('original_title') != title :
            return None
    '''
    '''
    elif response.get('results').get('original_title') == title :
        print(response.get('results').get('original_title'))
        # return response.get('results').get('id')
'''
'''
    title_list = []
    for i in range(len(response.get('results'))):
        if response.get('results')[i].get('title') == title :
            movie_id = response.get('results')[i].get('id')
        
            
    return movie_id         
'''
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None

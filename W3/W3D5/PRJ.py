import requests

students = ['gunhee','soobin','minji','yuyoung']

for name in students:
        
    URL = f'http://api.nationalize.io/?name={name}'
    response : requests.get(URL).json()
    print(response)
    print(response.get('country'))
    print(response.get('country')[0])
    print(response.get('country')[0].get('country_id'))

language 

'''
https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

<<api_key>>에 내 api 



#베이스 주소
https://api.themoviedb.org/3
/movie/{movie_id} # 영화일련번호
/movie/popular

&language=KR

get movie id

'''


# 베이스 주소
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular' # API 문서에서 적절하게 구성
api_key = ''

#params로 하면 URL을 한 줄로 합쳐줌
params = {
    'api_key' : ''
    'language' : 'ko-KR'
    'region' : 'KR'
}
response = requests.get(BASE_URL+path,params = params).json() # json으로 출력해달라
print(response)
print(response.get('result')[0])
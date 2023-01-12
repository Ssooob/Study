# 1 
string_list = [
    'Hello, Python!',
    '1일차 파이썬 공부 중',
    '2일차 파이썬 공부 중',
    '3일차 파이썬 공부 중',
    '4일차 파이썬 공부 중',
    '5일차 파이썬 공부 중',
]

with open('./01.txt', 'w') as f:
    for string in string_list:
        f.write(string + '\n')


#2
count = 0

with open('./data/fruits.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        count += 1

with open('./02.txt', 'w') as f:
    f.write(str(count))

#3
fruit_list = []
fruit_count = 0

with open('./data/fruits.txt', 'r') as f:
    fruits = f.readlines()
    for fruit in fruits:
        fruit = fruit.strip()
        if fruit[-5:] == 'berry':
            if fruit not in fruit_list:
                fruit_list.append(fruit)
                fruit_count += 1

with open('./03.txt', 'w') as f:
    # print(fruit_count)
    f.write(str(fruit_count) + '\n')

    for fruit in fruit_list:
        # print(fruit)
        f.write(fruit + '\n')

#4
fruit_dict = {}

with open('./data/fruits.txt', 'r') as f:
    fruits = f.readlines()
    for fruit in fruits:
        fruit = fruit.strip()

        if fruit not in fruit_dict:
            fruit_dict[fruit] = 1

        elif fruit in fruit_dict:
            fruit_dict[fruit] += 1

with open('./04.txt', 'w') as f:
    for fruit, count in fruit_dict.items():
        # print(fruit, count)
        f.write(f'{fruit} {count} \n')

#5
import json

# 아래 코드 수정 금지
movie_json = open('data/movie.json', encoding='UTF8')
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
new_movie = {
    'id': movie['id'],
    'title': movie['title'],
    'vote_average': movie['vote_average'],
    'overview': movie['overview'],
    'genre_ids': movie['genre_ids'],
}
print(new_movie)

#6
import json

# 아래 코드 수정 금지
movies_json = open('data/movies.json', encoding='UTF8')
movies_list = json.load(movies_json)

genres_json = open('data/genres.json', encoding='UTF8')
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
new_movie_list = []

for movie in movies_list:
    new_movie = {
        'id': movie['id'],
        'title': movie['title'],
        'poster_path': movie['poster_path'],
        'vote_average': movie['vote_average'],
        'overview': movie['overview'],
        'genre_ids': movie['genre_ids'],
    }
    new_movie_list.append(new_movie)

print(new_movie_list)

#7
import json

# 아래 코드 수정 금지
movie_json = open('data/movie.json', encoding='UTF8')
movie = json.load(movie_json)

genres_json = open('data/genres.json', encoding='UTF8')
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
genre_ids = movie['genre_ids']

genre_list = []
for genre_id in genre_ids:
    for genre_dict in genres_list:
        if genre_id == genre_dict['id']:
            genre_list.append(genre_dict['name'])

print(genre_list)

#8
import json

# 아래 코드 수정 금지
movie_json = open('data/movie.json', encoding='UTF8')
movie = json.load(movie_json)

genres_json = open('data/genres.json', encoding='UTF8')
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
genre_names = []
genre_ids = movie['genre_ids']
for genre_id in genre_ids:
    for genre_dict in genres_list:
        if genre_id == genre_dict['id']:
            genre_names.append(genre_dict['name'])

new = {
    'id': movie['id'],
    'title': movie['title'],
    'vote_average': movie['vote_average'],
    'overview': movie['overview'],
    'genre_names': genre_names,
}
print(new)

# 딕셔너리
## key와 value가 쌍으로 이루어지는 구조
* ```stdents = {'홍길동' : 100, '김철수' : 90}   stdents['홍길동'] = 80 ```
* dictionary 안에 list가 들어갈 수 있음
* 키와 값의 쌍을 추가할 수 있음
* 이미 해당하는 값이 있다면 기존 값이 변경됨
* list에 사용했던 함수 사용가능
* ***key값과 value 값 순회를 하기 위해 for와 name 변수를 활용***
* ***기본적으로 key값을 반환한다고 생각하면 될 듯***
</br>
</br>

* return
    * keys(): key로 구성된 결과 ```grades.keys()```
    * values(): value로 구성된 결과 ```grades.values()```
    * items() : (key, value)의 튜플로 구성된 결과 ```grades.items()```

     

```python
phone_book = {
    '피자헛' : '1588-5588',
    '전화번호' : '114',
    '이수빈' : '010 - 0000- 0000'
    '국밥집' : ['설렁탕','육개장','갈비탕'] # 이렇게 dictionary 안에 list가 들어갈 수 있음
    
    print({phone_book['피자헛']})
    >>> 1588-5588

}

stdents = {'홍길동' : 100, '김철수' : 90}
stdents['홍길동'] = 80
>> {'홍길동':80, '김철수':90} # 이런식으로 값이 바뀜

stdents['김영희'] = 95
>> {'홍길동':80, '김철수':90, '김영희': 95} # 추가할 수 있음

students.pop('홍길동') # key이름으로 진행해야함

for name in phone_book:
    # key만 반환
    print(name) 
    # value도 반환
    print(phone_book[name])


```

## 딕셔너리 순회 
```python
# 키 값만 순회
stdents = {'홍길동' : 100, '김철수' : 90}
for name in students:
    print(name)
    >> 홍길동
       김철수

# 키 값과 내용을 순회
for name in students:
    print(name,students[name])
    >> 홍길동 100
    김철수 90
```


# 모듈
* 모듈 : 다양한 기능(function)을 하나의 파일로
* 패키지 : 모듈이 여러개
* 라이브러리 : 다양한 패키지를 하나의 묶음으로
* pip : 이것을 관리하는 관리자 
* [파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)
</br>

* import를 통해 가져옴
* random (선택, 변수 반환, 무작위 정렬)
    ```python

    import random
    menu = ['햄버거', '초밥']

    # 하나 선택
    print(random.choice(menu))


    # random 변수 반환
    random.sample(population,k)
    # population = range
    # k개 반환
    numbers = range(1,46)
    lukey_numbers = random.sample(numbers,6)
    print(lucky_numbers)
    # 정렬
    print(sorted(lucky_numbers))


    #무작위로 정렬
    studentes = ['민욱','하나','민지','홍엽','현석']
    random.shuffle(studentes)


    ```

* datetime (현재 시간 반환, 날짜 생성)
    ``` python
    print(datatime.datatime.now())
    print(datatime.date(2023,1,5))

    today = print(datatime.date(2023,1,5))
    print(today.year)
    >> 2023
    print(today.day)
    >> 5

    end = datetime.date(2023,6,13)
    print(f'{end - today})
    >>160 days


    ```
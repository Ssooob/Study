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

## 중복 딕셔너리
* 딕셔너리 = {키1 : {키 A : 값 A}, 키2 : {키 B, 값 B}}
```python
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    }
}

# 입력을 사용자에게 받을 때의 예시
input1 = input("이름을 입력하세요 >")
input2 = input("전화번호를 입력하세요 >")
input3 = input("이메일을 입력하세요 >")
input4 = input("거주지를 입력하세요 >")

dict_variable = {
    input1 : {
        "전화번호" : input2,
        "이메일" : input3,
        "거주지" : input4,

    }
}

```
## 딕셔너리 정렬 
</br>

### dictionary key 오름차순 정렬
### sorted 함수 사용 -> sort()는 리스트에서 사용하는 거
### dictionary.items() 이용 -> key와 value가 튜플로 정리되어있는 애
```python
# origial dictionary
d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

# dictionary.items()
d1 = sorted(d.items())

print(f'sorted(d.items())      : {d1}')
>> [('app',20),('blockdmask',1),('car',99),('dream',0),('error',30)]
print(f'dict(sorted(d.items()) : {dict(d1)}')
>> {'app':20, 'blockdmask': 1, 'car': 99,'dream':0,'error':30 }

```
</br>

### dictionary value 오름차순 정렬
### lambda 식을 사용하여 튜플에서 1 번째 index를 기준으로 정렬
### dictionary.items() 이용
```python
# 람다 
(lambda x,y: x + y)(10, 20)
>>> 30
```


```python
d = {'A': 3, 'C': 1, 'G': 5, 'T': 2}
d.items()
>>> dict_items([('A', 3), ('C', 1), ('G', 5), ('T', 2)])

## 오름차순 정렬
sorted(d.items(), key=lambda x: x[1])
>>> [('C', 1), ('T', 2), ('A', 3), ('G', 5)]
 
## 내림차순 정렬
sorted(d.items(), key=lambda x: x[1], reverse=True)
>>> [('G', 5), ('A', 3), ('T', 2), ('C', 1)] 
```
[참조](https://korbillgates.tistory.com/171)
</br>
</br>


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
    print(f'{end - today}')
    >>160 days


    ```

    ## 해시테이블
    ### 딕셔너리는 리스트보다 시간 복잡도가 낮은 경우가 있음
    
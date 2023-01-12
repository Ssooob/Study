## a 가 있을 때 
* 반복문 
 ``` python 
 for char in word :
    if char == "a" :
        print(1)
```
* 조건문
```python
if 'a' in word
```
### a의 인덱스를 출력할 때
```python
# 반복문에서 숫자로 접근하고 싶을 때는 range를 쓰는게 좋음
for i in range(len(string)):
    if string[i] == 'e':
        print(i)
        break
else :
    print(-1)
```

### a의 인덱스를 삭제해야할 때 
* 문자열을 입력받고, 특정 문자를 제거한 결과를 출력해라
```python
# 빈 문자열 만드는 것이 중요
# 문자열도 연산이 가능
string = input("문자열을 입력하세요 >") # split이 안 들어감
result = ""

for i in string : 
    if i != 'e' :
        result += i 
print(result)

```

## a가 없을 때 
```python
locations =['서울','서울','대전','광주','서울','대전','부산','부산']
result = []

for location in locations :
    if location not in result :
        result.append(location)
print(result)
print(len(result))
```

# List
리스트에 값을 추가하자!
```python
num_list =[]
num_list.append(num)

# 혹은 list 이미 선언해주고 값 바꿔주기
num_list = [0,0]
num_list[0] = num1 
```

# 반복문

### element 범위
```python
num_list= [1,2,3,4,5]
sum = 0
for element in num_list :
    print(element," ") 
        >> 1 2 3 4 5
        # element는 element가 list에 반영이 되서 출력이 되는 것

num_list= [-1, -2, -3, -4, -5]
sum = 0
for element in num_list :
    sum += element # 여기서의 element는 이미 list에 반영이 된것 이기 때문에 element를 바로 sum해도 무방
    #sum += num_list[element-1] -> 이러면 num_list에 음수가 들어가서 에러남
print(sum)


```
### 짝수/ 홀수만 나오게 해라
1. for문에서 2씩 출력 
``` python
for i in range(1, num2,2): 
```
2. if 문
``` python
for i in range(1, num1): 
    if i %2 == 0 :
        continue
    else :
        print(i)
```

  </br>

# 조건문
* 부등호 여러개 가능 
```python
if  0<= a < 10 :
    ~

```

# 딕셔너리
### 출력물의 차이
### 요소의 갯수를 출력할 때는 딕셔너리가 좋음
```python
# 양식 자체가 출력
print(dict_variable.items())  
>> dict_items([('이름', '정우영'), ('생년월일', '19000101'), ('회사', '하이퍼그로스')])

# key와 value 만 출력 (for문 사용해야함)
for key, value in dict_variable.items():
    print(key, value)
>> 이름 정우영
>> 생년월일 19000101
>> 회사 하이퍼그로스

```

### 입력값에 따른 중복 값 출력
dictionary를 활용하면 각 문자가 몇개씩 나오는지 알 수 있음
```python
input1 = input("문자열을 입력하세요 >")
dict_variable = {}

for j in input1:
    cnt = 0
    for i in input1: 
        if j in i: 
            cnt +=1
    dict_variable[j] = cnt

for name in dict_variable:
    print(name,dict_variable[name])


# 다른 문제

#2 문자열을 입력받고, 각 단어의 등장 횟수를 출력 
# 이 때는 딕셔너리 쓰는게 좋음

string = input("입력:").split()
dict_var = {}

# count 안 쓸 때
# i는 종류 구분하기

for word in string:
    if word in dict_var :
        dict_var[word] += 1 
    elif word not in dict_var :
        dict_var[word] = 1

for key, value in dict_var.items():
    print(f"{key} {value}")
    
```


# String formatting
* 문자열을 변수를 활용하여 만드는 방법
```python
pi = 3.141592
print(f'반지름이 2일때 원의 넓이는 { pi*2*2}')
```

# 입력 값
## 여러 정수를 받을 때는 list 사용
``` python
a,b = list(map(int,input().split()))
print(a,b)

```
## 여러 문자열을 받을 때는 
```python
strings = input()
>> <class 'str'>

strings = input().split()
>> <class 'list'>

# type이 다르니, 유의해서 사용해야함

```


</br>
</br>

# 출력값
## 여러 문자열을 입력받고 출력 할 때 
* ```print(*string)```

```python
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
strings= input().split()
print(strings)
>> ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.']

#이를 문장으로 이어 도출해야하는 경우
print(*strings)
>> Lorem ipsum dolor sit amet, consectetur adipiscing elit.

```


# 파이썬 응용

## 조건문
```python 
# 절대값 출력하는 값
value = num if num >=0 else -num 
if num >=0:
    value = num
else :
    value = -num # 과 같음
```
```python

num = 2
result = '홀' if num%2 else '짝'

```
## List comprehension
```python
cubic_list = []
for number in range(1,4):
    cubic_list.append(number**3)
print(cubic_list) #랑 아래가 같음
```
```python

[number**3 for number in range(1,4)]

```

## Dictionart comprehention
```python
{number : number**3 for number in range(1,4)}
```

## 반복문
### enumerate()
* 인덱스와 객체를 쌍으로 담은 열겨형 객체 반환
    * (index,value) 형태의 tuple로 구성된 열거 객체를 반환
    ```python
    members = ['민수','철수','영희']

    for i in range(len(members)):
        print(f"{i} {members[i]}")
        # 랑
    for i, member in enmerate(members):
        print(i,member) 
    ```


### lambda
* 일회용 함수 사용할 때 -> 이름 없는 함수

```python
#2로 나눈 몫으로만 구성된
#[1,2]
numbers = [2,4]
def div_2(n):
    return n//2
print(list(map(div_2,numbers)))
```
```python
print(list(map(lambda n : n//2, numbers)))
# lambda : 이름 없는 함수
# 입력 해야하는 변수
# : n//2 : 동작할 함수
```
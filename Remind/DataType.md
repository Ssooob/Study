## Bool 형
### 참
"python", [1,2,3] {'a',1} 1
</br>

### 거짓
"",[],(),{},0,None

a = bool("")-> 이건 False
</br>
</br>

## 명시적 형변환
문자열+ 숫자열 (X)
``` python
int('3')+ 4 
>> 7
```

## String formatting
* 문자열을 변수를 활용하여 만드는 방법
```python
pi = 3.141592
print(f'반지름이 2일때 원의 넓이는 { pi*2*2}')
```


## in은 연산자로도 활용
in, not in 연산자는 데이터 안에 찾고자 하는 것이 있는지 없는지 
</br>확인하는 연산자
</br>
in 연산자의 결과는 bool형
</br>
데이터가 있는 경우 True, 없는 경우 False가 출력

```python
# 리스트
arr = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"'a' in arr : {'a' in arr}") # 문자열에 변수를 넣고 싶으면 f string formatting

# 튜플
t = (1, 2, 3, 4, 5)
print(f"99 not in t : {99 not in t}")

#딕셔너리
d = {"a": 123, "b": 456, "c": 789}
print(f"'a' in t : {'a' in d}")

```

## 튜플 (Tuple)
a = () 혹은 tuple()로 생성 
```python
a = (1,2,3,4)
print(type(a))
>>> <class 'tuple'

my_dict = {'name': '더 글로리', 'case':'송혜교'}
print(my_dict.keys())
>> my_dict.keys(['name','cast'])
print(my_dict.items())
>> my_dict.items([('name','더 글로리'),('cast','송혜교')])

```
리스트와 비슷 
</br>
***하지만 값 변경이 불가능하며 추가/ 삭제도 불가능***

</br>

## 세트(Set)
중괄호 혹은 set()을 통해 생성

***중복된 값을 저장할 수 없음***

순서가 없어 별도의 값에 접근할 수 없음 (인덱스 접근이 불가)

빈 set를 만들기 위해서는 set()를 반드시 활용해야함

값 추가는 .add() / 값 삭제는 .remove()

```python
blank_set = set()
{1,2,3,1,2}
>> {1,2,3}

# 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음
# 단, 순서가 무시되므로 순서가 중요한 경우 사용할 수 없음

my_list = ['서울','서울','대전','광주','서울','대전','부산','부산']

my_set = set()
my_set = set(my_list)

print(my_set)
>>> {'부산', '서울', '대전', '광주'}


```

## SET 
* 집합의 개념
* b_num = set(map(int,input().split()))
* 이런식으로 list처럼 사용해주면 됨

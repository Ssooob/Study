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
in, not in 연산자는 데이터 안에 찾고자 하는 것이 있는지 없는지 확인하는 연산자
in 연산자의 결과는 bool형
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

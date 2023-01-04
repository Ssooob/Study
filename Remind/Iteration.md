## range
```python
for x in range ()
# range () 에 그냥 list, string 이런 애들이 들어가도 됨, 처음부터 끝까지 해쥼
# 이어서 출력해줄거면 print(element, end= "")

range (a,b,c) # a부터 b-1까지 c 간격
enumerate # 인덱스와 원소로 이루어진 tuple로 만들어줌
```
## for문
```for 변수 in 리스트 (또는 튜플, 문자열)```
이때 변수는의 의미를 잘 이해해야함       
```python
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)
>>>
one 
two 
three
# i가 1이 아니고 one임 
# i가 리스트에 대입이 되는 것

```
## While 문
### 반복문 안쪽에 중단
```python
while (1) or (True): 
    break
```
### 조건
```python
while i <= 10 : 
    break
```
 

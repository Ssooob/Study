# 입력
### 여러 줄의 문자를 받을 때
while 함수 사용
``` python
while True :
    line = input()
    if a < 10 :
        break

```
[모음의 개수](https://www.acmicpc.net/problem/1264)

### 여러 자료형의 문자를 받을 때 
split을 사용
``` python
# 공백이 기준
a,b,c = input ("3개를 입력하세요 : ").split()
# 특정 문자가 기준
a,b,c = input ("3개를 입력하세요 : ").split(':')

>> 결과는 list로 나옴
```

### 여러 개의 입력을 받을 때 (동시 형변환)
```python
a,b,c = map(int, input("3개를 입력하세요 : ").split())
```

[럭비클럽](https://www.acmicpc.net/problem/2083)

# 문자열

### 특정 문자를 찾을 때 
반복문과 in **i in 'aeiouAEIOU'**
**이렇게 여러개의 문자를 한번에 찾을 수도 있음**
``` python
    cnt =  0
    for i in line :
        if i in 'aeiouAEIOU' : # 이런식으로 묶어서 받아도 됨
            cnt +=1

```
[모음의 개수](https://www.acmicpc.net/problem/1264)
[럭비클럽](https://www.acmicpc.net/problem/2083)

# 출력
### 여러 자료형 함께 출력
f-string 포매팅
변해야 하는 부분에 처리하면 더 쉽게 표현
```python
print(f"{name} Senior")

```
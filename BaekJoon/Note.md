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

# 숫자
## 자리수에 대한 계산
* %와 //를 응용하기 
* 계산을 하기 위해서는 이게 더 나음
```python
num = int(input())

lnum = num//10 # 2
rnum = num%10  # 6
lsnum = (rnum + lnum)%10 # 8 
num = (rnum*10) + lsnum # 68

```
[더하기 사이클](https://www.acmicpc.net/problem/1110)

</br>

# 출력
### 여러 자료형 함께 출력
f-string 포매팅
변해야 하는 부분에 처리하면 더 쉽게 표현
```python
print(f"{name} Senior")

```

# 문자열
## 문자열도 간단한 연산이 가능 

```python
# 문자열 S를 입력 받은 후, R번을 반복하여 새로운 문자열 출력
# example
# 3 ABC -> AAABBBCCC

# 이런식으로 for문을 많이 돌렸더니 시간 초과 나옴
new_string = list()
for t in range(1,T+1):
    R,S = input().split()
    R = int(R)
    # 모든 문자에 대해 돌려야 함
    for s in range(len(S)):
        # 원하는 갯수만큼 반복
        for r in range(1,R+1):
            new_string.append(S[s])
    print(*new_string)

# 다음과 같은 경우에 간단하게 쓸 수 있음
# 리스트도 아니고, 문자열로 표현 가능
# 심지어 리스트로 하면 문자열 간 띄어쓰기로 들어감

T = int(input())
for t in range(1,T+1):
    R,S = input().split()
    new_string = ''
    for s in S: # 이렇게 하면 s는 S의 요소가 됨
        new_string += int(R)*s

    print(new_string)

```
[문자열 반복](https://www.acmicpc.net/problem/2675)


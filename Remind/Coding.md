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

    

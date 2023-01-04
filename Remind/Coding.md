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
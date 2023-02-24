# 재귀함수
* 자기 자신을 다시 호출하는 함수
* python에서는 최대 재귀 깊이가 있어 오류날 수 있음
    * 스텍을 같이 활용할 수 있음
* 제한 없이 재귀 함수를 사용하고 싶다면 ? 
    * 제귀 제한을 느슨하게 만들거나
    * 별도로 스텍을 개체로 따로 만들어서 사용
* while이나 for가 아니더라도 사용할 수 있음
* 코딩 테스트 내에서는 무조건 종료 조건을 반드시 명시해야함
</br>

* 점화식같은 수식을 잘 활용할 수 있음

```python
def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()

# 종료 조건을 포함한 재귀 함수 예제
def recursive_function(i):
    if i == 100 :
        return # 그냥 return을 하면 됨 
    print(i,'번째 재귀함수를 호출합니다.')
    recursive_function(i+1)

recursive_function()

recursive_function()

```
## 팩토리얼 구현 예제
* n! = n * (n-1)!

```python
# 0! = 1! = 1

# for문을 사용한 경우
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result

# 재귀 함수를 사용한 경우

result = 1
def feacto_recur(n):
    if n <= 1 :
        return 1
    return n*feacto_recur(n-1) # n*(n-1)!

```

## 최대공약수 (유클리드 호제법)
* 두 개의 자연수에 대한 최대 공약수를 구하는 알고리즘
* A,B(A>B)가 있을 때 A를 B로 나눈 나머지를 R이라고 함
* 이 때 A와 B의 최대 공약수는 B와 R의 최대공약수와 같음
</br>

* MOD 연산 -> 두 값을 나눈 나머지를 구하는 연산
* 먼저, 큰 수를 작은 수로 나눈 나머지를 구함
* 그리고, 나눴던 수와 나머지로 또 MOD 연산
    * ex) 1112,695 
    * 1112 mod 695 = 417 
    * 695 mod 417 = 278
    * 417 mod 278 = 139
    * 278 mod 139 = 0
* 나머지가 0이 됐을 때, 마지막 계산에 활용된 139가 1112와 695의 최대공약수 

* 식을 구하는 과정이 반복적이면 재귀함수로 표현할 수 있음

```python
def gcd(a,b) :
    if a%b == 0 :
        return b 
    else :
        return gcd(b,a%b)

```


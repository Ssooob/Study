
# 동적계획법 (dynamic programming)
* 입력 크기가 작은 부분들의 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서, 보다 큰 크기의 문제를 해결
* 가장 최하위의 해답을 저장하고, 이를 기반으로 상위 문제를 해결
* Memoization 
    * 최하위 문제의 해답을 저장하는 것
    * 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 기술
    * 문제를 잘게 쪼갤 때, 부분 문제는 중복되어 재활용 됨
* 탑다운(위에서 아래), 보텀업(아래에서 위)

## Memoization 
* 한 번 구한 작은 문제에 대한 값을 저장해두었다가, 그대로 가져옴
* 배열, 리스트, 사전(dict) 자료형을 이용 
    * 연속적이지 않은 경우 

## 탑다운 vs 보텀업
* 탑다운 : 재귀함수를 호출 
* **보텀업 : 반복문으로 호출**
    * 결과 저장용 리스트 -> DP 테이블


## 다이나믹 프로그래밍의 조건
* 최적 부분 구조 (optimal substructure) 
    * 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아서 큰 문제를 해결
* 중복되는 부분 문제(overlapping subproblem)
    * 동일한 작은 문제가 반복적으로 해결해야 함

## 대표적인 문제 
* 피포나치 수열
    * 점화식이란 인접한 항들 사이의 관계식을 의미
    * 바로 앞에 있는 두 수의 합으로 구성
    * 배열이나 리스트를 이용해서 활용
```python
# 탑다운 (재귀함수)

d = [0]*100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)

    return d[x]


# 보텀업 (반복)
d = [0]*100

d[1] = 1
d[2] = 1
n = 99
for i in range(3,n+1):
    d[i]= d[i-1]+d[i-2]

print(d[n])

```
## 참고
* 특정한 문제를 완전탐색으로 접근했을 때 시간이 너무 오래거리면 다이나믹 프로그래밍을 적용할 수 있는지 중복여부를 확인해 보자
* 보텀업 방식으로 구현하는 것을 권장


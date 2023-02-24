# 스택 
* LIFO : 후입선출 
* list가 있을 때, append라는 method로써 뒤로 추가함 / pop을 하면 뒤에 있는게 나옴 
* 정해진 위치 (끝)에서 삽입, 삭제가 이루어짐
* list는 기본적으로 후입선출을 함
* 가장 마지막에 삽입된 자료가 가장 먼저 삭제 

# 큐 
* FIFO : 선입선출
* 뒤로 넣고, 앞으로 빼는 구조 
    * pop(0)으로 빠질 수 있지만 비효율적
* 한쪽 끝에서 삽입, 다른 한 쪽 끝에서 삭제 -> 양쪽으로 이루어짐
* 첫 원소를 (front), 끝 원소를 (rear) -> 큐는 들어올 때 rear로 들어오지만, 나올 때는 front로 빠짐
* 가장 먼저 들어온 front 원소가 가장 먼저 삭제
* deque를 사용해서 que를 사용 
    * deque가 속도가 더 빠름 

# 데크(deque)
* 스텍과 큐를 합친 형태
* 자유자재로 후입, 선입, 후출, 선출이 가능 

## 데크 함수 
* popleft == pop
* append 
* deque 만들기
    * card = deque([i for i in range(1,num+1)])
    * cards = deque(list(range(1,num+1)))
    * 위와 같이 해도 똑같음

</br>
</br>
</br>

    
# 이차원리스트
* 리스트를 원소로 가지는 리스트
```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# 이차원리스트 만들기 
# for문 활용
matrix = []
for _ in range(10):
    matrix.append([0]*10)
import pprint
pprint.pprint(matrix)

# M : 행, N : 열

for _ in range(N):
    matrix.append([0]*M)


M = 4
N = 3
matrix2 = [[0]*M]*N
print(matrix2)
matrix2[0][0] =1
print(matrix2)
# 이러면 모든 행의 1열에 1이 들어감
# 해당 리스트의 주소값 자체가 같은 주소를 가리킴
# 왜냐면 같은 리스트를 곱하기 했기 때문
print("=====================")

matrix3 = [[0]*M for _ in range(N)]
print(matrix3)
matrix3[0][0] = 1
print(matrix3)
# 얘가 원하는대로 입력

# 행렬의 크기가 입력으로 주어지는 경우
# 1
n,m = map(int,input().split()) # 8 7
matrix = [list(map(int, input().split())) for _ in range(n)]

#2 
n,m = map(int,input().split()) # 8 7
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

```
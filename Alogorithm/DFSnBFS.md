# DFS
* 깊이 우선 탐색
* 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
* 스택 자료구조, 혹은 재귀함수를 활용
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면, 그 노드에 스택을 넣고 방문 처리. 방문처리 하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

</br>

## DFS 동작 예시
1. 그래프를 준비 (방문 기준 : 번호가 낮은 인접 노드부터)
2. 시작노드 1을 스택에 넣음
3. 매번 최상단 노드를 확인하면서, 방문하지 않았다면 스택에 넣어줌
4. 1 -> 2(2 기준 인접하며 가장 작은 값) -> 7 -> 6 
5. 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5
* 깊이 우선을 탐색하기 때문에 먼저 가장 깊게 들어가고, 가장 깊게 들어갔다면 다시 방향을 틀어 방문하지 않은 노드들을 찾아서 감
* 항상 깊게 들어가기 떄문제 재귀함수와 함께 활용
* 인접노드가 없다면 스택에서 빼줌, 그 외에 것들은 일단 놔둠
* 왜냐면 놔뒀던 애들 기준으로 또 인접한 애들을 구해야하기 때문
* 

# BFS
* 너비 우선 탐색 
* 그래프에서 **가까운 노드부터 우선적으로 탐색**
* 큐 자료구조를 활용
* 특정 조건에서의 최단 거리 구하는 방법에 대해 많이 활용
1. 탐색 시작 노드를 큐에 삽입하고, 방문처리 
2. **큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리**
3. 2의 과정을 수행할 수 없을 때까지 반복

## BFS 동작 예시
1. 1을 큐에 넣고, 큐에서 꺼내서 인접한 노드를 다 큐에 넣음
2. 제일 밑에 큐를 꺼내고, 그 값과 인접한 노드를 다 큐에 넣음
3. 모든 곳을 방문처리 할 때까지 반복

## Visited 함수 활용 




# 자료 구조 복습
## 스택
* 박스를 쌓는 구조 
* 선입후출, 후입선출 구조 
* 박스를 꺼내려면 제일 위에 있는 박스부터 치워야 함 
* 별도의 라이브러리를 사용할 필요가 없음
* list.pop & list.append

```python
stack = []
stack.append(5)
stack.append(3)
stack.append(2)
stack.pop() # pop은 뒤에 있는 애를 뺌
stack.append(7)
stack.append(1)
stack.pop()
>> 5 3 7 

```

## 큐 (QUEUE)
* 식당 대기줄 
* 선입선출
* deque 라이브러리 활용
``` python 
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
>> 2 3 7


```
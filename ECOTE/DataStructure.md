# 큐
## 구조
* 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
* 줄을 서는 행위롸 유사
* FIFO(First In First Out)
* 특정 데이터의 인덱스를 지정해서 처리하지 않음 
* 가장 먼저 들어가 있는 데이터를 기준으로 데이터를 꺼내고 shift

## 큐는 언제쓰는 거?
* BFS(너비 우선 탐색)
* 우선순위 큐
</br>

## 알아둘 용어
* 데이터를 넣고(enqueue), 데이터를 빼는(dequeue) 역할을 함
</br>


## queue 라이브러리 제공
* put : 넣는거, get : 가져오는 거
```python
import queue

# Queue() : 가장 일반적인 큐 자료 구조
data_queue = queue.Queue

# 데이터를 넣을 때 
data_queue.put("data")
data_queue.put(1)
>> data, 1

# 데이터 사이즈 추출
data_queue.qsize()

# 데이터 추출
# 이 때는 인덱스를 지정하는게 아님 가장 먼저 넣은 애가 나옴
data_queue.get()

``` 
## LifoQueue()
* LIFO (Last In, First Out)
* 마지막에 넣은애가 첫번째로 나옴
```python
import  queue
data_queue = queue.LifeQueue()
data_queue.put("data")
data_queue.put(1)

data_queue.get()
>> 1
# 얘는 가장 마지막에 넣은 애가 나옴

```

## 우선순위 
* PriorityQueue()
* 시간 순이 아니고, 우선 순위를 정해 추출하는 것
* 각 value에 대한 우선순위는 tuple 형식으로 함께 저장
```python
import  queue
data_queue = queue.Priority.Queue()

# 우선순위가 같이 씀
data_queue.put((10,'Korea'))
data_queue.put((5,1))
data_queue.put((15,'China'))

data_queue.get()
>> (5,1) # 우선순위가 높은애가 제일 먼저 나옴
data_queue.get()
>> (10,'Korea')
```

## 실습
```python
queue_list = []
def enqueue(data)
    queue_list.append(data)

def dequeue(data)
    queue_list.pop(0)
    queue_list[0]
    del queue_list[0]
    return data


```
</br>

# 덱(deque)
* 큐는 데이터가 많을 때 선입선출이 비효율 -> 빼고 shift 해야해서
* 그래서 deque을 사용 
* **양방향으로 삽입과 삭제가 자유로운 큐 & 그리고 훨씬 빠름**

## 구조
* appendleft(): A[0]에서 넣음
* popleft() : A[0]에서 뻄
* append & pop : A[-1]에서 넣고 뺌
* from collections import deque



</br>
</br>

# 스택(Stack)
* 데이터를 제한적으로 접근할 수 있는 구조
    * 한쪽 끝에서만 자료를 넣거나 뻄
* **가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 구조**
    * 큐 : 가장 먼저 넣은 애를 가장 먼저 뺀다 (줄서기)
    * 스택 : 가장 마지막에 넣은 애를 가장 먼저 뺀다 (책쌓기)
* 예를 들어, 책을 막 쌓았는데, 제일 먼저 손이 가는 책은? 맨 위에 있는 책

## 구조
* LIFO(Last In First Out)
* push() : 데이터를 스텍에 넣기
* pop() : 데이터를 스텍에서 꺼내기 -> pop은 맨 뒤에 있는 애가 나옴
    * in Queue -> put(): 넣기, get(): 꺼내기
* 구현이 쉬우나, 자료 크기를 먼저 정해야함
    * 데이터를 쌓으려면 최대한 쌓으려는 공간을 먼저 확보해야함

## 스택은 언제 쓰나?
* 이전 작업의 기억 -> 뒤집기, 되돌리기, 되돌아가기
* 괄호매칭, 재귀함수, 백트래깅, DFS

```python
# stack을 list로 구현하기

stack_list = list()
def push(data):
    stack_list.apopend(data)

def pop():
    data = stack_list[-1] # 맨 뒤에 있는 애는 -1
    del stack_list[-1]
    return data
```

</br>
</br>

# 해쉬 테이블(Hash Table) & 딕셔너리
* 키(key)에 데이터(value)를 저장
* key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 줄어듦

## 딕셔너리 기본 문법
* 선언 : dic = {key1 : value, key2 : value ...}
* 삽입/수정 : dic[key] = value
* 삭제 : dic.pop(key,default)
* 조회 : dic[key] / dic.get(key,default)

## 딕셔너리 메서드
* .keys() : key 목록 반환
* .values(): value 목록 반환
* .items() : (key,value) 쌍 목록으로 객체 반환


</br>
</br>

``` python 
dic = {key1 : value, key2 : value ...}

a = {
    "name" : "jtke",
    "gender":"male",
    "address":"seoul"
}

print(a)
>> {'name':'jtke','gender':'male','address':'seoul'}

# 삽입 수정
dic[key] = value # 내부에 해당 key가 없으면 삽입, 있으면 수정
# 삭제
dic.pop(key) # 내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 KeyError 발생
dic.pop(key,default) # KeyError 방지

# 조회
dic[key]
dic.get(key)
dic.get(key,default) # KeyError 방지
print(a.get("phone","없음"))


```

</br>
</br>
</br>

# 힙 (Heap)
* 데이터에서 최대값과 최소값을 빠르게 찾기 위해서 고안된 이진트리
* 우선순위 큐와 같이 최대.최소값을 찾을 때 쓰임
* A[0]가 가장 작은 데이터, A[-1]가 가장 큰 데이터
* 이진트리의 구조를 활용

## 힙이 사용되어야하는 경우 ?
* 데이터가 지속적으로 정력되어야하는 경우
* 데이터 삽입/삭제가 빈번할 때

</br>

## 함수 
* 파이썬의 heapq 모듈
* minheap으로 구현되어있음 
* heapq.heapify() : 이미 생성해둔 리스트가 있다면, heapify 를 통해 즉각적으로 힙 자료형을 만들 수 있음 
* heapq.heappop(heap) : heap이라는 곳에서 가장 작은 값을 삭제
* heapq.heappush(heap,item) : heap이라는 곳에 item을 추가

</br>
</br>

```python
import heapq
numbers = [1,100,3,5,6,20]
heapq.heapify(numbers)
>> 1 5 3 100 6 20 
# 1 - 5 (100 / 6 ) 
#   - 3 - 20
heapq.push(numbers,0)
print(numbers)
>> 0 1 5 3 100 6 20 

heapq.heappop(numbers)
>> 0 

heapq.heappop(numbers)
>> 1 

```


## 큐와의 비교
* 큐 : 먼저 들어간 애가 먼저 나옴, 들어온 순서에 따라 
* 우선순위 큐 : 우선순위(중요도)를 기준으로 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식
    * 원래는 뒤에만 붙였는데, 중요도에 따라 정렬
    * 근데 중요도 자리를 찾아서 들어가는 것이기 때문에 계산복잡도가 높아짐
    * 하지만 최소, 최대값을 찾는다하면 항상 정렬이 되어있는 애니까 ! 그냥 맨 앞, 혹은 맨 뒤 값을 꺼내오면 됨




## 힙의 구조
* 최대 힙과 최소 힙으로 나뉨 
* 최대힙 : 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다 -> 가장 위에가 가장 크다 
* 최소힙 : 모 노드가 자식노드보다 같거나 작다 -> 가장 위에가 가장 작고
* 맨 위에 있는 애들이 최대/최소기 때문에 맨 위에 값만 빼오면 돼서 빠름
* 완전 이진트리의 형태를 가짐 -> 데이터를 넣을 때, 왼쪽부터 채워가게 되는 구조임 
* 완전 이진 트리 - 자식 노드가 2개인 형태 (왼 -> 오)


</br>
</br>
</br>

# 링크드리스트(Linked List)
* 배열의 단점은 미리 연결된 공간을 예약을 하고 그 안에 넣음
* linked list는 미리 예약하지 않고, 필요할 때마다 추가로 데이터를 넣을 수 있음
* (데이터 + 다음 데이터를 가리키는 주소) 가 노드로써 하나의 데이터를 의미 
* 노드(node) : 데이터 저장 단위(데이터 값, 포인터) 구성
* 포인터 (pointer) : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

```python 

# node 구현 -> class 를 만들어야함
# 데이터와 포인터를 넣어야하기 때문

class Node :
    def __init __(self,data):
        self.data = data
        self.next = None

        # self가 항상 앞에 붙지만, 인자로는 사용하지 않음

class Node :
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# 이 차이는, 데이터 뿐만 아니라, 주소값을 인자로 같이 넣어줄 때 활용하는 것 & 만약 인자가 data 하나라면 default를 None으로 간주하고 넣어주는 것


# node와 연결하기 

node1 = Node(1)
node2 = Node(2) # 이 객체들끼리는 연결이 안됨

node1.next = node2 # 이렇게 연결

# 전체 데이터를 불러오려면 첫번째 주소값을 알긴 알아야함
head = node1

#링크드 리스트로 데이터 추가하기
def add(data):
    node = head
    while node.next : # 이렇게 있으면, node.next가 있다면 실행
        node = node.next
    node.next = Node(data)

# 링크드 리스트 데이터 출력하기
node = head 
while node.next:
    print(node.data)
    node = node.next
print(node.data)

>> 1 2 3 4 5 6 7 8 9 

```

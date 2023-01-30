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
    
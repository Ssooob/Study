## 함수 종류
* map 
    * 첫번째 인자 (input)으로 함수를 받아서 
    * 두번쨰 인자 (input)인 반복 가능한 객체의 모든 요소에 적용
    ```python
    numbers = ['1','2','3']
    # 합을 구하려면 문자는 숫자가 되어야함
    # 새로운 리스트 생성

    new_numbers = []
    for number in numbers :
        new_numbers.append((int(number)))
    
    # 하지만 이를 함수로 대체 가능
    new_new_nmbers = map (int,numbers) 
    print(list(new_new_nmbers))
    >>[1,2,3]
    # int로 변환하는 함수를 받아서 numbers에 적용해라 
    ```
    </br>
### 리스트 관련 함수
* append 
    * 리스트 맨 마지막에 덧붙임
* pop
    * 맨 마지막 요소를 리턴하고 그 요소는 삭제한다 
    * ```a.pop(1)``` x번째 요소를 리턴하고 그 요소 삭제
* extend(x) 
    * x는 리스트만 올 수 있음
    * 원래 리스트에 x에 대한 리스트를 더함
    ```python
    a = [1,2,3]
    a.extend([4,5])
    a
    >>> [1, 2, 3, 4, 5]
    ```
* reverse 
    * 리스트 역순 정렬 
* index
    * 리스트에 x 값이 있으면 x의 인덱스를 반환
    ``` python
    a = [1,2,3]
    a.index(3)
    >> 2
    a. index(1)
    >> 0
    ```
* insert (a,b)
    * 리스트에 요소 삽입
    ```python
    a =[1,2,3]
    a.insert(0,4)
    a 
    >> [4,1,2,3] 
    ```
* remove
    * 요소 삭제 ?????? 
* count (x) 
    * x가 리스트 안에 몇 개 있는지 리턴


</br>
</br>
* divmod(a,b) 
    * 두 수를 받아서 몫과 나머지 리턴
* pow(base,exp,mod=None)
    * base의 exp 거듭제곱을 반환
    * mod가 있는 경우, base의 exp 거듭제곱의 모듈로 mod를 반환
* round 
    * 반올림

* all (iterable)
    * 모든 요소가 참이면 True
* any(iterable)
    * 어느 중 하나라도 참이면 True
    * 어느 하나라도 비어있으면 False

### 형변환 함수
* ord 
    * 유니코드 반환
* chr
    * 유니코드 대응되는 문자 반환
    ```python 
    ord(a)
    >> 97
    chr(97)
    >> a
    ```
* bin(이진), hex(16진), oct(8진)

* Sort 
    * 정렬


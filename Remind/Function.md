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
## 문자열 변경
* s.split(sep = None, maxsplit=-1)
    * 공백이나 특정 문자를 기준으로 분리
    * 문자열을 특정한 단위로 나눠서 리스트로 변환
    ``` python
    a = input()
    print(a)
    >>> 1 2
    # 1 각 숫자를 쪼개서 받을 거임
    input.split()
    # 2 각 쪼개서 받은 값들을 int로 일괄 변형할거임
    a,b = map(int,input().split)
    print(a+b)
    >>> 3
    ```
* 'separator'.join([iterable])
    * 구분자로 iterable을 합침
    ```python
    result = ['1','5','3']
    # 153을 출력해야함
        #1 print end
        print(result,end="")
    for a in result :

    ```
* s.replace(old,new[,count])
    * 바꿀 대산 글자를새로운 글자로 바꿔서 변환
    * count를 기정하면 해당개수만큼만 시행
    ```python
    print('coone'.replace('o','a'))
    >>> caane
    print('woooooowoo'.replace('o','!',2))
    >>> w!!oooowoo
    ```
* s.strip([chars])
    * 공백이나 특정 문자를 제거
    * 결과를 한 줄로 출력을 하거나 공백을 없애야한다
    ``` python
    result= ['1','5','3','4']
    print(''.join(result))
    >> 1534 
    >> print(' '.join(result))
    >> 1 5 3 4
    ```



### 리스트 관련 함수
* append 
    * 리스트 맨 마지막에 덧붙임
* pop
    * 맨 마지막 요소를 리턴하고 그 요소는 삭제한다 
    * ```a.pop(1)``` x번째 요소를 리턴하고 그 요소 삭제
    * ```pop(index)``` 해당 index값을 삭제
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
    * ```numbers[:,:,-1]``` 로도 조정 가능
* index(value)
    * 리스트에 x 값이 있으면 x의 인덱스를 반환
    ``` python
    a = [1,2,3]
    a.index(3)
    >> 2
    a. index(1)
    >> 0
    ```
* insert (index,value)
    * 리스트에 요소 삽입
    * index 값이 너무 크면 자동으로 맨 뒤에 작성
    ```python
    a =[1,2,3]
    a.insert(0,4)
    a 
    >> [4,1,2,3] 
    ```
* remove (value)
    * value 값 요소 삭제 
* count (x) 
    * x가 리스트 안에 몇 개 있는지 리턴
* sort
    * 정렬
    * 단어 길이로 정렬 -> sort(key = len)
* extend
    * list 자체를 추가
* clear
    * 리스트 자체를 삭제


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


## 문자열 탐색 및 검증

> find는 문자열에서 사용가능 


* s.find(x)
    * x의 첫번째 위치를 반환. 없으면 -1 반환
* s.index(x)
    * x의 첫번째 위치를 반환. 없으면 오류 발생
* s. isalpha ()
    * 알파벳 문자 여부
* s. isupper() / s.islower()
    * 대문자 여부 / 소문자 여부
* s.istitle()
    * 타이틀 형식 여부 ex. True String 

***is어쩌고함수들의 결과값은 Bool형***


</br>
</br>




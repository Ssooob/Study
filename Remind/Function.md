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


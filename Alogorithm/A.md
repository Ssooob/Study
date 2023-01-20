# 시간복잡도
* 순회하는 것보다 계산량으로 따지는게 더 효율
* 함수를 쓰는 것 -> 함수 당 계산량을 참고
* 자료 구조에 따라 똑같은 함수여도 계산 복잡도가 달라질 수 있음
## Log N 
* 이진탐색
</br>
</br>

# 리스트
## 배열 vs 연결리스트
* 다른 언어 배열에서는 해당 배열의 크기를 먼저 선언을 하고, 배열의 길이는 변경 불가능 -> 길이를 변경하고 싶다면 새로 생성 

## 연결리스트
* 데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료구조
    * 맨 처음 노드부터 처음부터 탐색
    * 데이터와 next 주소값이 함께 연결되어있는 구조 (linked list)
    * 그 다음으로 갈 데이터의 주소값을 미리 선언하는 것

## 리스트 컴프리헨션
* 리스트를 생성하는 방법 (for문보다 조금 더 빠름)
* 어떠한 리스트를 초기화 
* numbers = [i for i in range(5)]

# 문자열
* 변경이 불가
## 문자열 슬라이싱
    ```python
    s = 'abcdefghi' 
    s[a:b] # a부터 b-1까지
    s[2:5] >> 'cde'
    s[-6:-2] >> 'defg'
    
    s[:3] # 앞부터 N개 
    s[5:] # 뒤부터 N개
    
    ``` 
* 문자열 패턴일치를 보거나, 문자열을 만들거나 수정하는 문제들이 주로 나옴

## 문자열 메서드
* .split() : 문자열을 일정 기준으로 나누어 리스트로 반환
    ```python 
    word = "I_PLAY_THE_BALL"
    print(word.split("_"))
    >> ['I', 'PLAY', 'THE', 'BALL']
    ```
* .strip : 양쪽 끝의 문자들을 제거 
    ```python
    word = ' Hello world '
    print(word.strip()) 
    >> Hello world
    
    word = Hello worlddddddddd
    print(word.strip('d'))
    >> Hello worl
    ```
* .find() : 찾는 문자 -> 인덱스 반환
* .index() : 찾는 문자 -> 인덱스 반환
* .count() : 개수를 셀 문자
* .replace(기존문자, 새로운 문자) 
    * 특정 문자를 빈 문자열("")로 수정하여 해당 문자를 삭제한 것 같은 효과도 가능
* .join(문자열) : 각각 원소 사이에 특정 문자를 삽입한 새로운 문자열을 반환
    ```python
    word = ["euu","gmail.co.kr"]
    print("@".join(word))
    >> edu@gmail.co.kr
    word = ['h','a','p','p','y']
    print(''.join(word))
    >> happy
    word = 'hacking'
    print(','.join(word))
    >>h,a,c,k,i,n,g
    ```

* startswith & endswith : 해당 문자열이 앞과 끝에 있는지
    ```python
    'banana'.startswith('ba')
    >>  True
    'banana'.endswith('na')
    >>  True
    ```

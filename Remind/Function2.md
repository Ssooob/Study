## 함수
* 함수명()으로 호출
* def()로 선언
* return 값


## 함수의 결과값
* return
    * 함수 안에서 값을 반환하기 위해 사용하는 키워드
    * 명시적인 return이 없는 경우 : None
    * 여러 값을 return 하는 경우 : tuple
```python
def foo():
    return (1,2,3)
>> (1,2,3) #튜플

def boo():
    a = 1 +2
    print(boo())
>> None # 반환 X 
```

## 함수의 입력값
* parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
* argumemt : 함수를 호출할 때, 넣어주는 값
    * 위치에 따라 함수 내에 전달됨 ```add(x,y)<->add(2=x,3=y)```
    * 값을 지정해서 넘겨줄 수 있음
    
```python
def function(ham) : # parameter : ham
    return ham
function('spam') # argument : 'spam'
```

``` python
def add(x,y) :
    return x + y 

# 이 경우에는 parament = argument
add(x=2, y=5)
add(2,y=5) # 기본값 지정
# y 값이 지정되지 않으면 지정값을 사용한다

```
* 여러 값 받을 때
    * *사용
    ``` python
    # 입력값이 1 3 5 2 5 7 2
    def add(*numbers):
        print(type(nuumbers))
        return sum(numbers)
    
    print(add(1,3,5,2,5,7,2))
    ```
    * keyword 포함, dictionary 활용할 때
        * **활용
        ```python
        # **을 사용하려면 키워드와 함께 함수를 호출해야함

        def movie(**test):
            return test 
        
        print(movie(name='더글로리', wrriten = '김은숙'))
        >> {'name': '더 글로리', 'wrriten': '김은숙'}

        # open(file, mode = 'r', buffering  = -1 ... encoding = None)
        open('ReadMe.md','r',encoding= 'UTF8')
        # 앞 두개는 open의 순서에 맞추어 작성해 keyword를 작성 안 해댜ㅗ 되지만, encoding은 아님
        # 따라서 default로 지정되지 않은 값을 쓰고, 위치가 맞지 않다면 keyword를 함께 작성해야함

        ```
## 변수
* 지역변수


## Lambda
* lambda 매개변수 : 표현식
* (lambda 매개변수들 : 식)(인수들)
```python 
def hap (x,y) :
    return x + y
>>> hap(10,20)
30

>>> (lambda x,y : x+y)(10,20)
30

# map의 경우와 비교
map(함수, 리스트) # 리스트를 한 개씩 꺼내와서 해당 함수에 적용한 값들 도출
list(map(lambda x : x**2, range(5)))
# 0,1,2,3,4 를 하나씩 꺼내서 lambda라는 함수에 적용


```

## 정렬
1. sort 
    * list.sort()
2. sorted
    * sorted(list)
3. parameter (sorted(list,key))
    * 기본 값은 reverse = False(오름차순)
    * reverse = True (내림차순)
    * key 값 활용 
        * 정렬을 목적으로 하는 함수를 값으로 넣는다
        * lambda 활용
        ```python
        str_list = ['좋은하루','good_morning','굿모닝','niceday']
        >>> print(sorted(str_list), key = len)
        ['굿모닝','좋은하루','niceday','good_morning']

        >>> print(sorted(str_list),key = lambda x : x[1])
        ['niceday', 'good_morning', '굿모닝', '좋은하루']

        # 여러 요소를 가진 경우, 튜플로 사용
        tuple_list = [('좋은하루', 0),
                ('niceday', 1), 
                ('좋은하루', 5), 
                ('good_morning', 3), 
                ('niceday',5)]
        
        tuple_list.sort(key = lambda x : (x[0],x[1]))
        print(tuple_list)
        [('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]

        # 비교할 대상이 여러개인경우, 튜플로 우선순위를 정해줄 수 있음
        # 위와 동일
        a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]
        sort_score = sorted(a,key = lambda x : (x[0],-x[1]))
        # reverse 할 때는 -를 붙여주면 됨
        >>> [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]

        ```
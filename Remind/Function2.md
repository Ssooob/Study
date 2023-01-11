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

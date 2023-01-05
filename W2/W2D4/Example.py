# dictionary 생성 방법
    # 1. 빈 dict_variable{} 생성 -> dict_variable["key"] = value
    # 2. dict_variable = {"key1": "value1", "key2": "value2"}

#01
# dictionaly 생성 얘는 {}로 생성하고, 안 쪽은 []로 생성
dict_variable = {}

#key와 value를 입력, list 형태
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101" # 문자
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"])
print(dict_variable["생년월일"])
print(dict_variable["회사"])



#02 
dict_variable  = {"a": "A", "B": "b"}
# key와 value 추가
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"

print(dict_variable["a"]) 
print(dict_variable["D"]) 
print(dict_variable["b"]) 



#03
dict_variable = {}
dict_variable ["apple"] = 5000 # key apple value 숫자
dict_variable ["banana"] = 3000
dict_variable ["apple"] = 2000 # 저장된 값을 변경
dict_variable ["banana"] = dict_variable ["banana"] + 1000 # 정수로 저장했으니 연산이 가능

print(dict_variable["apple"] + dict_variable["banana"]) # banana 4000, apple 2000



#04
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

# 튜플로 나올 듯
for key in dict_variable :
    print(key, dict_variable[key])  

print("===========================")
# key만 나오는 경우
for key in dict_variable :
    print(key)  
print("===========================")
# value만 나오는 경우
for key in dict_variable :
    print(dict_variable[key])  

print("===========================")
print("===========================")

# for문 안 쓰고 함수로 출력
# keys(): key로 구성된 결과 ```grades.keys()```
# values(): value로 구성된 결과 ```grades.values()```
# items() : (key, value)의 튜플로 구성된 결과 ```grades.items()```

print(dict_variable.keys()) # dict_keys(['이름', '생년월일', '회사'])
print(dict_variable.values()) # dict_values(['정우영', '19000101', '하이퍼그로스'])
print(dict_variable.items())  # dict_items([('이름', '정우영'), ('생년월일', '19000101'), ('회사', '하이퍼그로스')])




#05
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)



#06 
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}
# key 값 하나 지정해서 출력
print("나이" in dict_variable)
# >> False : 나이라는 key는 없기 때문에 False가 출력



#07
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}
if "거주지" not in dict_variable: # 만약 거주지가 key에 없다면
    dict_variable["거주지"] = "서울특별시" # 거주지를 key로 추가해서 입력해라

print(dict_variable)



#08

# 리스트 선언
list_variable = []
try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

    # list_variable = [0,1,2] 밖에 없는데 list_variable[3]을 출력할 수 없음


#09
try:
    number = 1
    if number == 1 :
        print(number)
    
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

# 문법 오류 if 문 : 



#10
n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2 
        print(total) 
        print("===============") 
        # 
    elif number % 2 == 1:
        total += number + 1 * 3
        print(total) 
        print("===============") 

print("+++++++++++++++++++++") 
print(total) 

import datetime 


#01
string1 = input("문자열을 입력하세요 > ")
cnt = 0
for i in string1 :
    if i in 'e' :
        cnt +=1
print(cnt)



#02
string1 = input("문자열을 입력하세요 > ")
cnt = 0
for i in string1 :
    if i in 'aeiouAEIOU' :
        cnt +=1
print(cnt)


#03
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}
# datatime.date
today_date = datetime.date.today()
year = today_date.year
birth = int(dict_variable["생년"]) 
age = year-birth +1
print(age)


#04
dict_variable ={}
input1 = input("이름을 입력하세요 >")
dict_variable["이름:"] = input1
input2 = input("전화번호를 입력하세요 >")
dict_variable["전화번호:"] = input2
input3 = input("거주지를 입력하세요 >")
dict_variable["거주지:"] = input3

print(dict_variable)
for keys in dict_variable :
    print(keys, dict_variable[keys])
print("=============================")

# items 사용 경우
for key, value in dict_variable.items():
    print(key, value)



#05
input1 = input("이름을 입력하세요 >")
input2 = input("전화번호를 입력하세요 >")
input3 = input("이메일을 입력하세요 >")
input4 = input("거주지를 입력하세요 >")

dict_variable = {
    input1 : {
        "전화번호" : input2,
        "이메일" : input3,
        "거주지" : input4,

    }
}

print(dict_variable)


#06
input1 = input("문자열을 입력하세요 >")
dict_variable = {}

for j in input1:
    cnt = 0
    for i in input1: 
        if j in i: 
            cnt +=1
    dict_variable[j] = cnt

for name in dict_variable:
    print(name,dict_variable[name])


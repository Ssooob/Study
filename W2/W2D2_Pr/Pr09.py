num1= int(input("정수를 입력하세요 : "))

# 나누기 한 거
if num1 < 0 :
    print("False")
else :
    for i in range(1, num1): 
        if i %2 == 0 :
            continue
        else :
            print(i)


print("=================")

# 나누기 안 한거
num2= int(input("정수를 입력하세요 : "))

if num2 < 0 :
    print("False")
else :
    for i in range(1, num2,2): 

            print(i)






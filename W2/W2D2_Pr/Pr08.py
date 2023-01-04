num1= int(input("첫번째 숫자를 입력 : "))
num2 = int(input("두번째 숫자를 입력 : "))


# 빈 리스트에 할 수 있는 방법? 
num_list2= []
if num1 < num2 :
    num_list2.append(num1)
    num_list2.append(num2)

    for i in range(len(num_list2)) : 
        print(num_list2[i], end = " ")


elif num2 < num1 :
    num_list2.append(num2)
    num_list2.append(num1)

    for i in range(len(num_list2)) : 
        print(num_list2[i], end = " ")

else :
    print("False")


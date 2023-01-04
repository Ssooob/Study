
# 01
int1 = int(input("정수를 입력하세요 >"))
if int1 < 0 :
    int1 = (-1)*int1
print(int1)

# 02
num_list= [1,2,3,4,5]
j= 0
for i in num_list:
    j += 1
print(j)


#03
num_list= [-1, -2, -3, -4, -5]
sum = 0
for element in num_list :
    sum += element 
print(sum)


#04
number_list = [2, 3, 5, 7]
sum = 0
i = 0
for element in number_list :
    sum += element
    i +=1
average = sum/i
print(average)


#05
number_list = [-1, -2, 3]
mul = 1
for element in number_list :
    mul = mul*element 
print(mul)


#06
number_list = [1634, 387, -385]
max = -10000
for element in number_list :
    if element > max :
        max = element
print(max)



#07
number_list = [-723, 475, 28, 1]
min = 10000000
for element in number_list :
    if element < min :
        min = element
print(min)

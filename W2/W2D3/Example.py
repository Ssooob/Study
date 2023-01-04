
# Example 01

list_avaliable  = [0,1,2,3,4,5,6]
list_avaliable.pop() # 6 지우기
list_avaliable.append(7) # 뒤에 7과 8 추가
list_avaliable.append(8)

for element in list_avaliable[2:]:
    print(element, end = "") # 리스트의 값을 반환해라, index 2부터

# Example 02
for element in range(-2,10,2):
    print(element, end = " ")


# Example 03
a,b,c,d = 0,0,0,0
n = 10
for number in range(n):
    if number % 2 == 0 :
        a = a+1 # 2,4,6,8,10
    if number % 3 == 0 :
        b = b+1 # 3,6,9
    if number % 4 == 0 :
        c =c +1 # 4,8 

    if number % 5 == 0 :
        d =d +1 # 5,10
print(a,b,c,d)


# Example 04
i = 0 
while i <= 10:
    print(i)
    i = i+1



# Example 05
i = 0 
while i <=10:
    i = i+1
    print(i)



# Example 06
i = 0
while i <= 10:
    i = i+2
    print(i)



# Example 07
i = 0 
while True :
    print(i)
    i = i+1
    if i > 10:
        break


# Example 08
i = 0 
while True :
    print(i)
    if i > 10 :
        break
    i = i+1


# Example 09
list_variable = [0,1,2,3,4,5,6]
print(len(list_variable))


# Example 10
list_variable = [0,1,2,3,4,5,6]
print(sum(list_variable))


# Example 11
list_variable = [3,1,4,-3,9,7]
print(min(list_variable)-max(list_variable))

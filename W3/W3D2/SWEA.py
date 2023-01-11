
# 2029

T = int(input())

for t in range(1,T+1):
    a,b = list(map(int,input().split()))

    result1 = a//b
    result2 = a%b

    print(f"#{t} {result1} {result2}")


# 2071

T = int(input("Test case : "))
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    aver = round(sum(numbers)/len(numbers))

    print(f"#{t} {aver}")



# 1938
a,b = map(int,(input().split()))
print(f"{a+b}\n{a-b}\n{a*b}\n{a%b}")


# 2046
a = int(input())
print('#'*a)


#2068

# MAX 함수를 사용하는 경우

T = int(input())
for t in range(1,T+1):
    numbers= list(map(int, input().split()))
    result = max(numbers)
    
    print(f"#{t} {result}")

# MAX 함수 사용하지 않는 경우

T = int(input())
for t in range(1,T+1):
    numbers= list(map(int, input().split()))
    max_val = -1000000
    for number in numbers :
        if number > max_val :
            max_val = number
    result = max_val
    
    print(f"#{t} {result}")



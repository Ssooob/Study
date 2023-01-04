n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if n < 0:
        break


# element의 range는 10에서 -10까지 1씩 줄어드는 것
# 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")

# test case
T = int(input())
for t in range(1,T+1):
    date = input()
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:len(date)+1])

    if year > 0000 :
        if month == 0 or month >=13:
            print(f"#{t} {-1}")

        elif month == 2 :
            if 1 <= day <= 28:
                print(f"#{t} {date[0:4]}/{date[4:6]}/{date[6:len(date)+1]}")
            else : 
                print(f"#{t} {-1}")
        elif month == 4 or 6 or 9 or 11 :
            if 1 <= day <= 30:
                print(f"#{t} {date[0:4]}/{date[4:6]}/{date[6:len(date)+1]}")
            else : 
                print(f"#{t} {-1}")
        elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12 :
            if 1 <= day <= 30:
                print(f"#{t} {date[0:4]}/{date[4:6]}/{date[6:len(date)+1]}")
            else : 
                print(f"#{t} {-1}") 

    else : 
        print(f"#{t} {-1}")


    ## 광배님 코드
    T = int(input())

data = [-1 ,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for t in range(1, T + 1):
    ymd = input()

    y = ymd[:4]
    m = ymd[4:6]
    d = ymd[6:]

    if int(m) > 12 or int(d) > data[int(m)]:
        result = -1
    else:
        result = f'{y}/{m}/{d}'
    print(f'#{t} {result}')

# 민욱님 코드

li=[]
for k in range(1,13):
    if k == 2:
        li.append(range(1,29))
    elif k==4 or k==6 or k==9 or k==11:
        li.append(range(1,31))
    else:
        li.append(range(1,32))
    

for i in range(1,int(input())+1):
    n = input()
    if int(n[4:6]) == 0 or int(n[4:6]) > 12:
        print(f'#{i} -1')
    else:
        if int(n[6:8]) in li[int(n[4:6])-1]:
            print(f'#{i} {n[:4]}/{n[4:6]}/{n[6:8]}')
        else:
            print(f'#{i} -1')
            
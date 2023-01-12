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

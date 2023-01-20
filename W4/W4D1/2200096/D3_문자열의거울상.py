import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1,T+1):
    string1 = list(input())
    string = string1[::-1]
    for s in range(len(string)) :
        if string[s] == 'q' :
            string[s] = 'p'
        elif string[s] == 'p':
            string[s] = 'q'
        elif string[s] == 'b':
            string[s] = 'd'
        elif string[s] == 'd':
            string[s] = 'b'
    result = "".join(string)
    print(f"#{t} {result}")
  


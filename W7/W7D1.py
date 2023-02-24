import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

# 10769 행복한지 슬픈지

string = input()
happy,sad,none = 0,0,0
emotion = []
cnt = 0
for i in range(len(string)-2) :
    if string[i] == ':' and string[i+1] == '-' :
        if string[i+2] == ')':
            happy += 1
        elif string[i+2] == '(':
            sad += 1
if happy == 0 and sad == 0:
    result = 'none'
else :
    if happy > sad :
        result = 'happy'
    elif sad > happy :
        result = 'sad'
    elif sad == happy :
        result = 'unsure'
print(result)

'''
# count 를 쓴 경우
string = input()
happy_cnt = string.count(':-)')
sad_cnt = string.count(':-(')
if happy_cnt > sad_cnt :
    print('happy')
elif happy_cnt < sad_cnt :
    print('sad')
elif happy_cnt == sad_cnt == 0 :
    print('none')
elif happy_cnt == sad_cnt :
    print('unsure')
'''

'''
# 2455 지능형 기차
inout,total= [],[]
peo = 0
for t in range(4):
    inout.append(list(map(int,input().split()))) 
    tin=inout[t][1]
    tout = inout[t][0]
    peo -= tout
    peo +=tin 
    
    total.append(peo)
print(max(total))
'''


# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline


# 7113 rectangle
import sys
sys.setrecursionlimit(10**9)
a,b = map(int,input().split())
cnt = 0 
def rect_cut(a,b):
    global cnt
    if a == b :
        cnt += 1
        return cnt
    else :
        if a > b :
            a -= b
            cnt += 1
            rect_cut(a,b)
        elif a < b :
            b -= a
            cnt += 1
            rect_cut(a,b)
rect_cut(a,b)
print(cnt)


# 16505 별
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input()) # 2의 제곱만큼 줄 수가 나옴
g = [[' ']*(2**n) for _ in range(2**n)]

print(g)
def star(n,i,j):
    if n == 0:
        g[i][j] = '*'
        return
    if n == 1:
        g[i][j],g[i][j+1],g[i+1][j] = '*','*','*' # 점 3개 찍기
    
    # 2부터 
    # 가장 작은 모듈..을 봤을 때 n = 1 임 얘가 자꾸 반복됨
    star(n-1,i,j)
    star(n-1,i+2**n//2,j)
    star(n-1,i,j+2**n//2)

star(n,0,0) # 맨 처음 점 
for i in g:
    print(''.join(i).rstrip())

'''

'''
counting_star = int(input())

# 밤 하늘에 퍼ㅓㅓㅓㄹ..... 
# 먼저.. 모듈 단위로 만들고 이걸 쌓아야할 듯

floor = 0
def printing_star(cs,floor):
    global num
    if cs == 0: 
        num = 1 
        return module_star(num)

    elif cs == 1 : 
        num = 2
        return module_star(num)
    else : 
        num = 4
        if floor == 2^(cs-2) :
            return
        else :
            module_star(num)   
            floor +=1
            print(floor)        
            printing_star(cs,floor)
            

        # return module_star(num)


def module_star(num):
        # 모듈
    for i in range(num,0,-1):
        if i == 3 :
            ps = '*'*i # 문자열은 인덱싱으로 수정 못 함
            ps = list(ps) # 리스트로 바꿔준 다음
            ps[1] = ' ' # 값 바꾸고 
            print(''.join(ps)) # join으로 print
        else : 
            print('*'*i)

printing_star(counting_star,floor)
'''

# 17829 222-풀링
'''
m = int(input())
matrixs = [list(map(int,input().split())) for _ in range(m)]

def find_2nd(m,arr):
    if m == 1 :
        return print(arr[0][0])
    new_arr = [[]for _ in range(m//2)]
    
    for i in range(0,m,2):
        for j in range(0,m,2):
            new_arr[i//2].append(sorted([arr[i][j],arr[i][j+1],arr[i+1][j],arr[i+1][j+1]])[2])
    
    return find_2nd(m//2, new_arr)
find_2nd(m,matrixs)

'''

'''
# 17829 222-풀링
# 잘 못 품.. 2번째로 큰 수가 아니라.. 2x2인 애인줄 앎
m = int(input())
matrixs = []
for k in range(m):
    matrixs += list(map(int,input().split()))
#matrixs = [list(map(int,input().split())) for _ in range(m)]

second_idx = 0

print(matrixs)
def find_2nd(m,matrix):
    # 처음에 8+1  
    second = []
    start_idx = m+1
    # 2 x 2 -> 1개, 4 x 4 -> 4개, 8 x 8 -> 16개 
    # (2/2)*(2/2), (4/2)*(4/2), (8/2)*(8/2)
    for i in range(int((m/2)*(m/2))):
        second.append(matrix[start_idx])
        print(second)
        if int(i % (m/2)) == int(m/2)-1 : # and i > 0
            #print('--',i % (m/2))
            start_idx += int((m*2)-2*((m/2)-1))
        else : 
            #print('-',i)
            start_idx += 2 
        #print('st',start_idx)
    m2 = int(m/2)
    if m2 == 1 :
        return print(second)
    find_2nd(m2,second) 

    

find_2nd(m,matrixs)
'''
# 16974 레벨 햄버거 
# 런타임에러..Name error
# 50 4321098765432109 이거 컴퓨터에서 돌리면 memory 에러남
'''
sys.setrecursionlimit(10**9)
N,X = map(int,input().split())
burger = [0]
burger[0]= 'P'
cnt = 1
def burger_cnt(arr,n,x,cnt):
    #print(arr[-1])
    new_arr1 = arr[-1]
    new_arr = []
    new_arr.append('B'+str(new_arr1)+'P'+str(new_arr1)+'B')
    #print(new_arr)
    #arr.append('B'+str(arr[-1])+'P'+str(arr[-1])+'B')
    cnt += 1
    if cnt == n+1 :
        # print_arr = arr[-1]
        return print(new_arr[0][0:x].count('P'))
        # return print(print_arr[0:x].count('P'))
    else :
        burger_cnt(new_arr,n,x,cnt)
burger_cnt(burger,N,X,cnt)
'''

# 1074 Z
'''
N,R,C = map(int,input().split())

def find_rc(n,r,c):
    # matrix 생성
    mat = [[0]*(2) for _ in range(2)]
    # print(mat)

    # 4 x 4 기본형
    for i in range(2):
        for j in range(2):
            if 
find_rc(N,R,C)
'''

# 23304 아카라카
'''
import sys
sys.setrecursionlimit(10**9)
s = sys.stdin.readline().rstrip()

def aka_pel(s):
    P_flag = False
    len_s = len(s)

    if len_s == 1:
        P_flag = True
        return P_flag
    
    if s == s[::-1]:
        P_flag = aka_pel(s[:len_s//2])
    
    return P_flag


if aka_pel(s):
    print('AKARAKA')
else:
    print('IPSELENTI')
'''


'''
sen_list = list(input())
aka = []

def aka_pel(total_list) :# flist,llist
    global aka
    fir_list,last_list = [],[]
    # 짝 홀수 확인
    if len(total_list)%2 != 0 :
        sen_len1,sen_len2 = int(len(total_list)/2),int(len(total_list)/2)+1
    elif len(total_list)%2 == 0 :
        sen_len1,sen_len2 = int(len(total_list)/2),int(len(total_list)/2)
    print(sen_len1,sen_len2)
    
    fir_list = ''.join(total_list[0:sen_len1])
    last_list = ''.join(total_list[sen_len2:])
    print(fir_list,last_list)

    if fir_list != last_list :
        print('IPSELENTI')
    elif fir_list == last_list:
        aka_pel(fir_list)
        aka_pel(last_list)
        if len(fir_list) == len(last_list) == 1:
            print('AKARAKA')

aka_pel(sen_list)

'''


    




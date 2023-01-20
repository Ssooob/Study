# 기본 코드
import sys
sys.stdin = open("input.txt", "r")


# 2789 유학금지
colleage = input()
for c in colleage :
    if c in 'CAMBRIDGE' :
        colleage = colleage.replace(c,"")
print(colleage)


# 더 짧은 코드로.. for문으로 replace 더 잘 이용하기
for i in 'CAMBRIDGE' : # 문자열 직접 넣어도 되니까
    colleage = colleage.replace(i,"")
print(colleage)


# 2675 문자열 반복

T = int(input())
for t in range(1,T+1):
    R,S = input().split()
    new_string = ''
    for s in S: # 이렇게 하면 s는 S의 요소가 됨
        new_string += int(R)*s

    print(new_string)


# 10988 팰린드롬인지 확인하기
# reverse와 아닌것이 같아야함
string = input()
r_string = string[::-1]
if string == r_string :
    print(1)
else :
    print(0)



#17249 태보태보총난타

nanta = input()
left = nanta.find('(')
right = nanta.find(')')
c_left = nanta[:left].count('@')
c_right = nanta[right:].count('@')

print(c_left, c_right)


# 애초에 불러올 때 나눠서 불러올 수 있음(구글링 참고)
R,L = input().split('(^0^)')
print(R.count('@'),L.count('@'))




# 2941 크로아티아 알파벳
string = input()
croat = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cro_cnt = 0
for i in croat:
    string = string.replace(i,"#")
print(len(string))


# 10809 알파벳 찾기
# 알파벳 개수 26개

string = list(input())
alpha = [-1]*26
idx = 0
for s in string :
    if alpha[ord(s)-ord('a')] != -1 :
        idx +=1
        pass
    else :
        alpha[ord(s)-ord('a')] = idx
        idx +=1
print(*alpha)

# find 함수 사용한 방법 (구글링)
S = input()
arr = list(range(97, 123))

for i in arr:
    print(S.find(chr(i))) 
    # 어차피 find는 해당 문자가 없으면 -1을 반환


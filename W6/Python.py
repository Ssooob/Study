matrix = []
for _ in range(10):
    matrix.append([0]*10)
import pprint
#pprint.pprint(matrix)

M = 4
N = 3

matrix2 = [[0]*M]*N
print(matrix2)
matrix2[0][0] =1
print(matrix2)
# 이러면 모든 행의 1열에 1이 들어감
# 해당 리스트의 주소값 자체가 같은 주소를 가리킴
# 왜냐면 같은 리스트를 곱하기 했기 때문
print("=====================")

matrix3 = [[0]*M for _ in range(N)]
print(matrix3)
matrix3[0][0] = 1
print(matrix3)
# 얘가 원하는대로 입력



list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    # 만약 음수라면 contibue로 그냥 함수를 통과해버리는데
    if element < 0 :
        continue

    # 양수라면 print라는 함수를 작동
    print(element,end ="")

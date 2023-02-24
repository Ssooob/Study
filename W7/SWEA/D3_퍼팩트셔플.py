import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    deck_len = int(input())
    deck_list = list(input().split())
    odd_flag = False
    
    # deck 길이 나눠주기
    if deck_len%2 != 0 :
        a_part = int(deck_len/2 +1) 
        b_part = int(deck_len - a_part)
        odd_flag = True

    elif deck_len%2 == 0 :
        a_part,b_part = int(deck_len/2),int(deck_len/2)

    a_part_deck,b_part_deck = deck_list[:a_part],deck_list[a_part:]

    # 나눠주기 (작은 수로 해야함 -> b_part 길이)
    shuffle_deck = []
    for p in range(b_part):
        shuffle_deck.append(a_part_deck[p])
        shuffle_deck.append(b_part_deck[p])
    if odd_flag == True :
        shuffle_deck.append(a_part_deck[-1])

    result = " ".join(shuffle_deck)

    print(f'#{t} {result}')
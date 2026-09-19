# def solution(a,b,c,d):
#     dice = [a,b,c,d]
#     set_dice = set(dice)
#     l_dice = list(set_dice)
#     answer = 0

#     if len(set_dice) == 1:
#         answer = 1111 * l_dice[0]
#     elif len(set_dice) == 2:
#         count = 0
        
#         for i in range(len(dice)):
#             if l_dice[i] == dice[i]:
#                 cont += 1
        
#         if count == 2:
#             a = (l_dice[0] + l_dice[1])
#             b = abs(l_dice[1] - l_dice[0])
#             answer = a * b
#         if count == 3:
#             answer = (10 * l_dice[0] + l_dice[1])**2
        
#     elif len(set_dice) == 3:
#         answer = l_dice[1] * l_dice[2]
#     else:
#         answer = min(l_dice)

#     return answer

def solution(a, b, c, d):
    dice = [a, b, c, d]
    set_dice = set(dice)
    l_dice = list(set_dice)

    if len(set_dice) == 1:
        answer = 1111 * l_dice[0]

    elif len(set_dice) == 2:
        p = l_dice[0]
        q = l_dice[1]

        if dice.count(p) == 2:
            answer = (p + q) * abs(p - q)

        elif dice.count(p) == 3:
            answer = (10 * p + q) ** 2

        else:
            answer = (10 * q + p) ** 2

    elif len(set_dice) == 3:
        answer = l_dice[1] * l_dice[2]

    else:
        answer = min(dice)

    return answer
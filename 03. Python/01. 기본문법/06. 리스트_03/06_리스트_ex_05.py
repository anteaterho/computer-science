
# def calc(usage):
#     price = 0
#     if usage > 0 and usage <= 20:
#         price = 430
#     elif usage > 21 and usage <= 30:
#         price = 570
#     elif usage >= 31:
#         price = 840

#     result = usage * price
#     return result

# ret = calc(20)
# print(ret)

#수학적 표현
# def solution(usage):
#     if usage <= 20:
#         return usage*430
#     elif usage <= 30:
#         return 20*430+(usage-20)*570
#     return 20*430+10*570+(usage-30)*840

# usage=int(input("사용량 : "))
# ret = solution(usage)
# print(ret)

#반복문 표현
def solution(usage):
    sum=0
    while usage:
        if usage > 30:
            sum+=840
        elif usage > 20:
            sum += 570
        else:
            sum += 430
        usage=usage-1
    return sum

usage=int(input("사용량 : "))
ret = solution(usage)
print(ret)
items = [5,3,4,2,3,2]

# a = []
# b = []
# for i in range(0,len(items)):
#     if items[i] > 3:
#         a.append(items[i])
#     else:
#         b.append(items[i])


# print(a, b)
def solution(items):
    normal, small = 0,0

    for i in items:
        if i <= 3:
            small += i
        else:
            normal += i
    # if normal > small:
    #     return normal
    # return small
    return max(normal, small)
    
ret = solution(items)
print(ret)


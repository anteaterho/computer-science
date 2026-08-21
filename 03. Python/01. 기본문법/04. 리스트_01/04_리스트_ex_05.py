a = "Life is too short"

# print("문장의 길이 :", len(a))

# cnt = 0
# for i in range(len(a)):
#     str = " "
#     if a[i] == 's':
#         #print("Yes")
#         cnt += 1
# # if cnt > 0:
# #     str = "Yes "
# # else:
# #     str = "No "
# if cnt == 0:
#     print('No', cnt)
# else:
#     print('Yes', cnt)

# #print(str, cnt)

if 's' in a:
    print('Yes', a.count('s'))
if 's' not in a:
    print('No', a.count('s'))

print(a[8:14])
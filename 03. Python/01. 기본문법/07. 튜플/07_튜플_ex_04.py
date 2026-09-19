# [07. 튜플] ex_04
# 학습 목표: 튜플에서도 되는 집계 함수와 언패킹 — a,b,c,*d 와 a,*b,c

nums = (20,70,90,100,66,151,45)
# print(max(nums))
# print(min(nums))

# a=list(nums)
# a.sort()
# print(a)
# print(sum(a[1:-1]))

# print(sum(nums)-max(nums)-min(nums))

a = list(nums)
a.sort()
print(a)

#언팩
a,b,c,*d=nums
print(a,b,c,d)

a, *b, c = nums
print(a,b,c)

print(sum(b))
nums = [12, 23, 132, 47, 5, 63, 72]

# a = sorted(nums)
# print("Max: ", a[-1])
# print("Min: ", a[0])

# b=0
# for i in range(len(nums)):
#     b+=nums[i]
# print("Sum: ", b)
# c = b/len(nums)
# print("Avg: {:.2f}" .format(c))

print("Max: ", max(nums))
print("Min: ", min(nums))
print("Sum: ", sum(nums))
print("Avg: {:.2f}" .format(sum(nums)/len(nums)))

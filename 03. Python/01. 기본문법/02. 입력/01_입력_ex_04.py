import math

a = input("첫 번째 숫자: ")
b = input("두 번째 숫자: ")

print("{} * {} = {}".format(a, b, int(a) * int(b)))
print("{} / {} = {:.2}".format(a, b, a/b))
#print("{} / {} = {}".format(a,b, int(a/b)))
#print("{} / {} = {}".format(a,b, (a//b)) #몫은 //
     
#print("{} / {} = {}".format(a, b, math.floor(int(a) / int(b), 2)))
#print("{} % {} = {}".format(a, b, int(a) % int(b)))

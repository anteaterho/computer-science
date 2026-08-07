'''
a = input("나이를 입력하세요 : ")
b = int(a) + 2
c = " "
if b > 18:
    c = "adult"
else:
    c = "teenager"

print("I'm {} years old. \n 2years later, I'll a be {}.".format(a, c))
'''

age = input("나이를 입력하세요 : ")
print("I'm {} years old.".format(age))

if age >= '20':
    print("I'm adult.")
elif 14 < age:
    print("youth")


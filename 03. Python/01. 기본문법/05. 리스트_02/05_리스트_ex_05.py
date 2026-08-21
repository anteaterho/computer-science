import random

#names = ["Newton", "Faraday", "Edision", "Einstein", "Obama"]
names = 'Newton, Faraday, Edision, Einstein, Obama'.split(', ')

names.append("Tesla")

#print(names)

#n=random.randrange(0,len(names))
#print("내가 가장 좋아하는 인물은", names[n], "입니다.")
n=random.choice(names)
print('내가 가장 좋아하는 인물은"{}"입니다.'.format(n))
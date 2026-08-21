import random

station = "용산행, 문산행, 대화행, 서울역행, 홍대입구행, 인천공항행".split(", ")

# print(station)
# n = random.choice(station)

# print('이번 열차는 "{1}!! {0}!!" 열차가 들어오고 있습니다.'.format(n,'해운대역행'))

#n = random.choices(station,k=2) # 중복이 허용이 됨
n = random.sample(station,2) # 중복이 안 일어남.
print(n)
import random

station = "용산행, 문산행, 대화행, 서울역행, 홍대입구행, 인천공항행".split(", ")

a = random.choice(station)

print('이번 열차는 "{}!! {}!!" 열차가 들어오고 있습니다.'.format(a, a))
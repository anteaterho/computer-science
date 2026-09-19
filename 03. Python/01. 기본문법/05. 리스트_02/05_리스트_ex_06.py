# [05. 리스트_02] ex_06
# 학습 목표: split과 random.choice 응용 — 전철 안내방송 만들기

import random

station = "용산행, 문산행, 대화행, 서울역행, 홍대입구행, 인천공항행".split(", ")

a = random.choice(station)

print('이번 열차는 "{}!! {}!!" 열차가 들어오고 있습니다.'.format(a, a))
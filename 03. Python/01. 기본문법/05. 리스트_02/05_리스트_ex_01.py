# [05. 리스트_02] ex_01
# 학습 목표: replace()로 필요 없는 글자를 지우고 슬라이싱으로 날짜·시간 나누기

from datetime import datetime

data = str(datetime.now())[:19]
#print(data)
data=data.replace('-','')
data=data.replace(' ','').replace(':','')
print(data)

print("="*7, "숫자 해독", "="*7)
print("날짜 : {}년 {}월 {}일" .format(data[:4], data[4:6], data[6:8]))
print("시간 : {}시 {}분 {}초" .format(data[8:10], data[10:12],data[12:]))
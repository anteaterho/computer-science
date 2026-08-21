from datetime import datetime

data = str(datetime.now())[:19]
#print(data)
data=data.replace('-','')
data=data.replace(' ','').replace(':','')
print(data)

print("="*7, "숫자 해독", "="*7)
print("날짜 : {}년 {}월 {}일" .format(data[:4], data[4:6], data[6:8]))
print("시간 : {}시 {}분 {}초" .format(data[8:10], data[10:12],data[12:]))
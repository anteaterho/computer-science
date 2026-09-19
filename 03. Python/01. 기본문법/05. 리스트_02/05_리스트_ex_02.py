# [05. 리스트_02] ex_02
# 학습 목표: 일정 간격으로 건너뛰며 문자열 읽기 — range의 증가폭 활용

data = "3봄수일이민시오아청나잘앞보하정네자오요"

a = ""
b = ""
c = ""

for i in range(0,len(data)-2,3):
    a=a+data[i]
    b=b+data[i+3]
    c=c+data[i+2]
    
#for j in range(0,len(data),3):
#    b+=data[j]

#for k in range(2,len(data),3):
#    c+=data[k]

print(a)
print(b)
print(c)
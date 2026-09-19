# [02. 입력] ex_07
# 학습 목표: while True + break로 정해진 횟수만큼 반복하기, end= 옵션


#for i in range(1, 16):
#    print(i)


i = 1
while(1):
    print(i, end = " ") # end 는 커서 를 다음 줄로 내리지 않고, 공백으로 띄우게 하는 옵션
    i = i +1
    if i > 15:
        break

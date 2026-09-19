# [02. 입력] ex_02
# 학습 목표: 정수와 실수 입력을 구분해 받고(int/float) 결과를 소수점 형식으로 출력하기

m = input("추의 질량 : ")
g = input("중력가속도 : ")

p = int(m) * float(g)
print("힘 {} * {} = {:.2f}[n]".format(m,g,p))
# [01. 출력] ex_08
# 학습 목표: 여러 값의 합과 평균을 구하고 소수점 자릿수를 지정해 출력하기

K = 90;  M = 85; E = 100

Sum = K + M + E
Avg = Sum / 3

print ("Kor :", K)
print ("Math :", M)
print ("Eng :", E)
print ("Sum : ", Sum)
print ("Avg : %.2f" % Avg) # 올바른 % 포매팅 사용
# print(f"Avg {Avg:.2f}") # f-string을 사용하는 것이 더 권장됩니다.
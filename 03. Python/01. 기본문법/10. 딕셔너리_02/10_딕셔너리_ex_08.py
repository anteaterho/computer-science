# [10. 딕셔너리_02] ex_08
# 학습 목표: 딕셔너리를 조회표로 써서 주문받기 — while 반복과 키로 값 찾기

menu = {"americano":4000, "latte":4500, "green tea":3500, "milk tea":4000}

#print(menu)

price = 0
#orders = []

while True:
    order = input("주문을 해주세요 : ")
    #orders.apend(order)
    price += menu[order]
    condition = input("주문을 추가하시겠습니까?(y/n)?")
    if condition == 'y':
        continue
    if condition =='n':
        break
    
print(price)

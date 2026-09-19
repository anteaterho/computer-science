ice = {'탱크보이':1200, '폴라포':1200,'빵바레':1800, '월드콘':1500, '메로나':1000}

#ice내 items의 총가격을 출력

print(len(ice))

#for i in range(len(ice)):

#names=list(ice.keys())
price=list(ice.values())
#kk = list(ice.items())
print(type(price))
print(sum(price))
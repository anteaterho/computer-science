# [09. 세트_02] ex_03
# 학습 목표: 두 명단 비교하기 — update()로 여러 개 추가, discard()로 삭제

java = ["Tesla", "Faraday", "Maxwell", "Ampere"]
python = ["Hertz", "Edison", "Einstein", "Tesla", "Maxwell"]

j = set(java)
p = set(python)

# print( j & p)
# print(j - p)
# print(p-j)
# print(j | p)

# j = list(j)
# p = list(p)
# p.add("Joule")
# p.add("Newton")
p.update({"Joule", "Newton"})
p.discard("Edison")
print(list(p))

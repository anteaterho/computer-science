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

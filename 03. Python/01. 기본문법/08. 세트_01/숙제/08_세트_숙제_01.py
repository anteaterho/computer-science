# [08. 세트_01] 숙제_01
# 학습 목표: 순서를 지키면서 중복 제거하기 — not in으로 걸러 새 리스트에 담기

language = ['C++', 'Python', 'C', 'Python', 'C++', 'C']

result = []

for i in language:
    if i not in result:
        result.append(i)

print(result)


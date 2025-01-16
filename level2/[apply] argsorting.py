# 내림차순으로 정렬을 하는데 value로 정렬하는 것이 아니라 그 값의 인덱스로 정렬하는 것

# 어떤 데이터들의 포인트가 가장 가까운지, 먼지를 판단할 때 사용
# KNN, K-mean clustering에서 사용

import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }")

sort_indices = []
for _ in range(n_students):
    max_score, max_score_idx = None, None
    for score_idx, score in enumerate(scores):
        if score_idx in sort_indices:
            continue
        if max_score == None or score > max_score:
            max_score = score
            max_score_idx = score_idx
    sort_indices.append(max_score_idx)

print(f"{sort_indices = }")
# 합격자 리스트 만들기

import random

n_students = 20
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }")

scores_pass = []
for score in scores:
    if score < threshold:
        continue
    scores_pass.append(score)
print(f"{scores_pass = }")
# 암 진단했을 때, 음성(Negative): 0 | 양성(Positive): 1
# Negative, Positive는 모델이 예측한 prediction 값임

# False Positive: 모델이 positive라고 예측했는데 실제로는 Negative인 경우
# False Negative: 모델이 Negative라고 예측했는데 실제로는 Positive인 경우

import random

n_data = 100
labels = [random.randint(0, 1) for _ in range(n_data)]
predictions = [random.randint(0, 1) for _ in range(n_data)]
print(f"{labels = }")
print(f"{predictions = }\n")

n_FP, n_FN = 0, 0
for label, pred in zip(labels, predictions):
    # if label != pred:
    #     if pred == 1: n_FP += 1
    #     else: n_FN += 1

    if label != pred and pred == 1:
        n_FP += 1
    elif label != pred and pred == 0:
        n_FN += 1

print(f"{n_FP = }")
print(f"{n_FN = }")
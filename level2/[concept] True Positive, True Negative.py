# 암 진단했을 때, 음성(Negative): 0 | 양성(Positive): 1
# Negative, Positive는 모델이 예측한 prediction 값임

# True Positive: 모델이 postive라고 예측했는데 실제로 positive인 경우
# True Negative: 모델이 Negative라고 예측했는데 실제로 Negative인 경우

import random

n_data = 100
labels = [random.randint(0, 1) for _ in range(n_data)]
predictions = [random.randint(0, 1) for _ in range(n_data)]
print(f"{labels = }")
print(f"{predictions = }\n")

n_TP, n_TN = 0, 0
for label, pred in zip(labels, predictions):
    # if label == pred:   # True
    #     if label == 0:  # negative prediction
    #         n_TN += 1
    #     else:           # positive prediction
    #         n_TP += 1

    if label == pred and label == 0:
        n_TN += 1
    elif label == pred and label == 1:
        n_TP += 1

print(f"{n_TP = }")
print(f"{n_TN = }")
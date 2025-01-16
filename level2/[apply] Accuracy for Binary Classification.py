# label 값과 모델이 각 데이터에 대해 예측한 prediction 값이 주어질 때
# 그 모델의 accuracy를 계산하기

# segmentation 분야에서 고차원 tensor 직접 accuracy를 계산하는 경우가 있을 것임

import random

n_data = 100
labels = [random.randint(0, 1) for _ in range(n_data)]
predictions = [random.randint(0, 1) for _ in range(n_data)]
print(f"{labels = }")
print(f"{predictions = }\n")

n_corrects = 0
for label, pred in zip(labels, predictions):
    if label == pred:
        n_corrects += 1
accuracy = n_corrects / n_data
print(f"{accuracy = }")
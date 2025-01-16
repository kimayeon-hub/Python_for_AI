import random

n_data = 100

labels = [random.randint(0, 1) for _ in range(n_data)]
predictions = [random.randint(0, 1) for _ in range(n_data)]
print(f"{labels = }")
print(f"{predictions = }\n")

n_TP, n_TN, n_FP, n_FN = 0, 0, 0, 0
for label, pred in zip(labels, predictions):
    if label == pred:   # True
        if pred == 0: n_TN += 1
        else: n_TP += 1
    else:   # False
        if pred == 0: n_FN += 1
        else: n_FP += 1
print(f"{n_TP = } | {n_FP = }")
print(f"{n_FN = } | {n_TN = }")

# 절댓값의 리스트 만들기 with for loop, if-else statement
import random

n_data = 10
data = [random.randint(-10, 10) for _ in range(n_data)]
print(data)

data_abs = []
for d in data:
    if d >= 0:
        data_abs.append(d)
    else:
        data_abs.append(-d)
print(f"{data_abs = }")
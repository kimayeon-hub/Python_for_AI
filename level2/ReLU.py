# Rectified Linear Unit (ReLU)
# 딥러닝에서 activation function으로 ReLU를 사용함

# 값이 0보다 크면 그대로, 0보다 작으면 0을 반환


# if, else statement로 구현
num = int(input("Enter a number: "))

if num > 0:
    relu = num
else:
    relu = 0
print(f"ReLU({num}) = {relu}")


# for loop + if-else statement로 구현
import random

n_data = 10
data = [random.randint(-10, 10) for _ in range(n_data)]
print(f"{data = }")

relu_values = []
for d in data:
    if d >= 0:
        relu_values.append(d)
    else:
        relu_values.append(0)
print(f"{relu_values = }")
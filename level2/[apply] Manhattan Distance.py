# Manhattan Distance (L1 Distance)
# Euclidean Distance (L2 Distance)에서 루트와 제곱 대신, 절댓값을 사용함

import random
from dis import distb

vec_dimension = 5
u = [random.randint(-5, 5) for _ in range(vec_dimension)]
v = [random.randint(-5, 5) for _ in range(vec_dimension)]
print(f"{u = }")
print(f"{v = }")

manhattan_dist = 0
for u_el, v_el in zip(u, v):
    diff = u_el - v_el
    if diff >= 0:
        manhattan_dist += diff
    else:
        manhattan_dist += -diff
print(f"{manhattan_dist = }")
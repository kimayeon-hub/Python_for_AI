# 학생 수 입력 받아, 학생 수 만큼 랜덤으로 점수 생성해서 리스트에 넣기

import random

n_students = int(input("Enter a number of students: "))
scores = [random.randint(0,100) for _ in range(n_students)]
print(f"{len(scores) = }")
print(scores)
import random

n_students = int(input("Enter a number of students: "))
scores = [random.randint(0,100) for _ in range(n_students)]
print(f"{len(scores) = }")
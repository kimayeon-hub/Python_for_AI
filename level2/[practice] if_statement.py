# 자신의 점수를 입력하고 그 시험에 합격을 했는지 불합격인지 검사
threshold = 80
score = int(input("Enter a your score: "))
if score >= threshold:
    print("Pass!")
else:
    print("No Pass!")


# 절댓값 구하기
num = int(input("Enter a number: "))
if num > 0:
    abs_val = num
else:
    abs_val = -num
print(f"absolute value of {num} is {abs_val}")


# 3n cycle을 구현
for num in range(10):
    if num % 3 == 0:
        print(f"{num} is 3n")
    elif num % 3 == 1:
        print(f"{num} is 3n + 1")
    else:
        print(f"{num} is 3n + 2")


# 합격생들의 점수만 모으기
import random

n_students = 20
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }")

scores_pass = []
for score in scores:
    if score >= threshold:
        scores_pass.append(score)
print(f"{scores_pass = }")


# 합격생과 불합격생의 평균점수 구하기
import random

n_students = 20
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }\n")

scores_pass, scores_fail = [], []
for score in scores:
    if score >= threshold:
        scores_pass.append(score)
    else:
        scores_fail.append(score)
print(f"{scores_pass = }")
print(f"{scores_fail = }\n")

score_pass_mean = sum(scores_pass) / len(scores_pass)
score_fail_mean = sum(scores_fail) / len(scores_fail)
print(f"{score_pass_mean = :.2f}")
print(f"{score_fail_mean = :.2f}")

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


# Prime Number
num = int(input("Enter a number: "))

IS_PRIME = True
for divisor in range(2, num):
    if num % divisor == 0:
        IS_PRIME = False
        break;

if IS_PRIME:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# Prime Number (위의 코드보다 더 좋게 만들어 봄. for 문을 반복하는 횟수를 줄임)
num = int(input("Enter a number: "))

IS_PRIME = True
for divisor in range(2, int(num**0.5)):
    if num % divisor == 0:
        IS_PRIME = False
        break;

if IS_PRIME:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# List Comprehension + If Statement
import random

n_students = 100
threshold = 80

scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }\n")

scores_pass = [score for score in scores if score >= threshold]
scores_fail = [score for score in scores if score < threshold]
print(f"{scores_pass = }")
print(f"{scores_fail = }")


# 짝수, 홀수 구분하기 with list comprehension
import random

n_data = 100
data = [random.randint(0, 100) for _ in range(n_data)]
print(data, '\n')

even_data = [d for d in data if d % 2 == 0]
odd_data = [d for d in data if d % 2 == 1]
print(f"{even_data = }")
print(f"{odd_data = }")

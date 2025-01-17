# # n을 넘는 최초의 누적합
# threshold_sum = int(input("Enter a number: "))
#
# cum_sum = 0
# i = 0
# while cum_sum <= threshold_sum:
#     cum_sum += i
#     i += 1
#     print(f"{i} - {cum_sum}")
#
#
# # while statement + break
# i = 0
# while True:
#     i += 1
#     print(i)
#
#     if i == 10:
#         break
#
#
# # n을 넘는 최초의 누적합 2
# threshold_sum = int(input("Enter a number: "))
#
# cum_sum, i = 0, 0
# while True:
#     if cum_sum > threshold_sum:
#         break
#     cum_sum += i
#     i += 1
#     print(f"{i} - {cum_sum}")
#
#
# # 유저한테 프로그램 종료시키기
# while True:
#     user_input = input("q to quit: ")
#     print(user_input)
#     if user_input == 'q':
#         break
#
#
# # 점수를 차례대로 출력하기
# import random
# n_students = 100
# scores = [random.randint(0, 100) for _ in range(n_students)]
#
# score_idx = 0
# while True:
#     user_input = input("q[quit], n[next]: ")
#     if user_input == 'q':
#         break
#     elif user_input == 'n':
#         print(f"{score_idx}-th score: {scores[score_idx]}")
#         score_idx += 1
#
#
# # 최초의 1이 아닌 약수
# num = int(input("Enter a number: "))
#
# divisor = 2
# while True:
#     if num % divisor == 0:
#         print(f"first {divisor = }")
#         break
#     divisor += 1


# 최초 n 명의 합격자들의 인덱스 구하기
import random

n_students = 10
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

n = int(input("Enter a number: "))
pass_students = []
score_idx = 0
while len(pass_students) < n and len(scores) != 0:
    score = scores[0]
    if score >= threshold:
        pass_students.append(score_idx)

    scores.pop(0)
    score_idx += 1
print(pass_students)
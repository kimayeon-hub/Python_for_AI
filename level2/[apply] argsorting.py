# 정렬을 하는데 value로 정렬하는 것이 아니라 그 값의 인덱스로 정렬하는 것

# 어떤 데이터들의 포인트가 가장 가까운지, 먼지를 판단할 때 사용
# KNN, K-mean clustering에서 사용


# # 내림차순 argsorting with membership and continue
# import random
#
# n_students = 10
# scores = [random.randint(0, 100) for _ in range(n_students)]
# print(f"{scores = }")
#
# sort_indices = []
# for _ in range(n_students):
#     max_score, max_score_idx = None, None
#     for score_idx, score in enumerate(scores):
#         if score_idx in sort_indices:
#             continue
#         if max_score == None or score > max_score:
#             max_score = score
#             max_score_idx = score_idx
#     sort_indices.append(max_score_idx)
# print(f"{sort_indices = }")

# 내림차순 argsorting (membership and continue 사용하지 않고 구현해 보기)
import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }")

scores_tmp = scores.copy()  # 원본 데이터의 손실을 막기 위해 deep copy해서 데이터 사용하기
sort_indices = []
for _ in range(n_students):
    max_score, max_score_idx = None, None
    for score_idx, score in enumerate(scores_tmp):
        if max_score == None or score > max_score:
            max_score = score
            max_score_idx = score_idx
    sort_indices.append(max_score_idx)
    scores_tmp[max_score_idx] = 0   # 넣은 최댓값은 -1으로 바꿔서 다음 for loop에서 이 값을 최대값으로 절대 만들 수 없게 설정
print(f"{sort_indices = }")


# # 오름차순 argsorting
# import random
#
# n_students = 10
# scores = [random.randint(0, 100) for _ in range(n_students)]
# print(f"{scores = }")
#
# sort_indices = []
# for _ in range(n_students):
#     min_score, min_score_idx = None, None
#     for score_idx, score in enumerate(scores):
#         if score_idx in sort_indices:
#             continue
#         if min_score == None or score < min_score:
#             min_score = score
#             min_score_idx = score_idx
#     sort_indices.append(min_score_idx)
# print(f"{sort_indices = }")
# dictionary는 왜 사용하는가?
# list보다 보기 좋은 형태로 data를 관리할 수 있음
# 서로 다른 정보를 묶을 때는 list는 사용하기 부적합함. 그 값이 무엇을 의미하는지 알기 어려움

# import random
#
# n_students = 20
# scores = [random.randint(0, 100) for _ in range(n_students)]
# print(f"{scores = }\n")
#
# # 평균, 분산, 표준편차 구하기
# score_mean = sum(scores) / len(scores)
# score_var = sum([(score - score_mean)**2 for score in scores]) / len(scores)
# score_std = score_var**0.5
#
# # 최댓값, 최솟값 구하기
# max_score, max_score_idx = None, None
# min_score, min_score_idx = None, None
# for score_idx, score in enumerate(scores):
#     if max_score == None or score > max_score:
#        max_score = score
#        max_score_idx = score_idx
#     elif min_score == None or score < min_score:
#         min_score = score
#         min_score_idx = score_idx
#
# # 평균, 분산, 표준편차, 최댓값, 최솟값, 인덱스 한 번에 저장
# score_info = [score_mean, score_var, score_std,
#               max_score, max_score_idx,
#               min_score, min_score_idx]
# print(f"{score_info = }")


# dictionary를 사용하면 편리함
# dictionary의 구조 = Key:Value
score_info = {'mean': 10,'var': 100,'std': 10,
              'max': 10,'max_idx':1,
              'min': 2,'min_idx': 5}
print(type(score_info))

print(score_info['mean'])   # key를 사용해 검색 ((dictionary의 장점))
print(score_info['var'])
print(score_info['std'])
print(score_info['max '])
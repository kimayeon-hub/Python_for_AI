# dictionary에 원소 추가
score_info = {}
print(score_info)

score_info['mean'] = 10
print(score_info)

score_info['var'] = 100
print(score_info, '\n')


# scores의 정보들을 dictionary에 저장하기
import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }")

score_info = {}

score_info['mean'] = sum(scores) / len(scores)
score_info['var'] = sum((score - score_info['mean'])**2 for score in scores) / len(scores)
score_info['std'] = score_info['var']**0.5

max_score, max_score_idx = None, None
min_score, min_score_idx = None, None
for score_idx, score in enumerate(scores):
    if max_score == None or score > max_score:
        max_score = score
        max_score_idx = score_idx
    elif min_score == None or score < min_score:
        min_score = score
        min_score_idx = score_idx
score_info['max'] = max_score
score_info['max_idx'] = max_score_idx
score_info['min'] = min_score
score_info['min_idx'] = min_score_idx

print(score_info, '\n')


# 최댓값, 최솟값 구하기 with dictionary
import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }")

max_min_dic = {'max': None, 'max_idx': None, 'min': None, 'min_idx': None}
for score_idx, score in enumerate(scores):
    if max_min_dic['max'] == None or score > max_min_dic['max']:
        max_min_dic['max'] = score
        max_min_dic['max_idx'] = score_idx
    elif max_min_dic['min'] == None or score < max_min_dic['min']:
        max_min_dic['min'] = score
        max_min_dic['min_idx'] = score_idx
print(max_min_dic, '\n')



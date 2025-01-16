import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }")

scores_tmp = scores.copy()
scores_sort = []

while len(scores_tmp) != 0:
    min_score, min_score_idx = None, None
    for idx, score in enumerate(scores_tmp):
        if min_score == None or score < min_score:
            min_score = score
            min_score_idx = idx
    scores_sort.append(min_score)
    scores_tmp.pop(min_score_idx)
print(f"{scores_sort = }")
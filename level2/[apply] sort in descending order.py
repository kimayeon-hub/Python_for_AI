# scores에서 큰 수부터 하나씩 뽑아서 scores_sort에 넣는 방법으로 정렬

import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores = }")

scores_tmp = scores.copy()  # scores가 변경되지 않게 원본 데이터를 복사해 사용하기
scores_sort = []

while len(scores_tmp) != 0:
    # 최댓값의 인덱스 구하기
    max_score, max_score_idx = scores_tmp[0], 0
    for idx, score in enumerate(scores_tmp):
        if score > max_score:
            max_score = score
            max_score_idx = idx

    # 최댓값 넣어주기
    scores_sort.append(max_score)
    scores_tmp.pop(max_score_idx)

print(f"{scores_sort = }")
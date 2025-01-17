# histogram: 각각의 데이터의 빈도수를 bar plot으로 그린 표

import random

n_students = 100
threshold = 80
interval = 20
scores = [random.randint(0, 100) for _ in range(n_students)]

hist_dict = {key:0 for key in ['0', '20', '40', '60', '80']}
for score in scores:
    # if score >= 0 and score < 20:
    #     hist_dict['0'] += 1
    # elif score >= 20 and score < 40:
    #     hist_dict['20'] += 1
    # elif score >= 40 and score < 60:
    #     hist_dict['40'] += 1
    # elif score >= 60 and score < 80:
    #     hist_dict['60'] += 1
    # elif score >= 80 and score < 100:
    #     hist_dict['80'] += 1
    # else: continue

    bin_idx = score // interval # hist_dict의 key 값들의 인덱스를 나타냄
    if bin_idx == 5:    # score가 100인 경우 처리
        bin_idx = 4
    hist_dict[str(bin_idx * interval)] += 1

print(hist_dict)



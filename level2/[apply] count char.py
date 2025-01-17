# 글자 수 세기
# 자연어 처리, 스팸 메일 필터링 등에서 많이 사용되는 기술

test_string = 'aabbbbccccd'

count_char_dict = {}
for ch in test_string:
    # if count_char_dict.get(ch) == None:
    #     count_char_dict[ch] = 1
    # elif count_char_dict.get(ch) != None:
    #     count_char_dict[ch] += 1
    count_char_dict[ch] = count_char_dict.get(ch, 0) + 1
print(count_char_dict)


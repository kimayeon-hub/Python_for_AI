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


# counting char 추가 연습
# 여러 줄의 넣을 때는 따옴표 3개(''' or """) 사용하면 됨
test_string = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

cnt_dict = {}
for char in test_string:
    cnt_dict[char] = cnt_dict.get(char, 0) + 1
print(cnt_dict)
test_list = [1, 2, 3]
test_list2 = test_list  # shallow copy
test_list3 = test_list.copy()   # deep copy

# 이때 test_list와 test_list2가 같은 객체를 가리킬까? 서로 다른 객체를 가리킬까?
# shallow copy가 일어났기 때문에 같은 객체를 가리킴

# test_list를 수정하면 test_list2의 값도 바뀌게 됨
test_list[1] = 200
print(f"{test_list = }")
print(f"{test_list2 = }")
print(f"{test_list3 = }")


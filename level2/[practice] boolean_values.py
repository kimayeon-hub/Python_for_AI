# 리스트가 비어 있는지 아닌지 검사
test_list = []
print(len(test_list) == 0)

# 리스트에 들어 있는 원소의 개수가 입력 값보다 작은지 검사
test_list = [1, 2, 3]
threshold_input = int(input("Enter a threshold: "))
print(len(test_list) < threshold_input)
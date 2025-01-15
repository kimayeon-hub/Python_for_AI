# Rectified Linear Unit (ReLU)
# 딥러닝에서 activation function으로 ReLU를 사용함

# 값이 0보다 크면 그대로, 0보다 작으면 0 반환
# if, else statement로 구현

num = int(input("Enter a number: "))
if num > 0:
    relu = num
else:
    relu = 0
print(f"ReLU({num}) = {relu}")
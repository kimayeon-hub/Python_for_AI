# 자신의 점수를 입력하고 그 시험에 합격을 했는지 불합격인지 검사
threshold = 80
score = int(input("Enter a your score: "))
if score >= threshold:
    print("Pass!")
else:
    print("No Pass!")


# 절댓값 구하기
num = int(input("Enter a number: "))
if num > 0:
    abs_val = num
else:
    abs_val = -num
print(f"absolute value of {num} is {abs_val}")


# 3n cycle을 구현
for num in range(10):
    if num % 3 == 0:
        print(f"{num} is 3n")
    elif num % 3 == 1:
        print(f"{num} is 3n + 1")
    else:
        print(f"{num} is 3n + 2")

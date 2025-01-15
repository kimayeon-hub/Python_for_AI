# 자신의 점수를 입력하고 그 시험에 합격을 했는지 불합격인지 검사
threshold = 80
score = int(input("Enter a your score: "))
if score >= threshold:
    print("Pass!")
else:
    print("Fail!")

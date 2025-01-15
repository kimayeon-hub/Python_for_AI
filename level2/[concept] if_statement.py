# 입력된 수가 5보다 큰지 아닌지 검사
num = int(input("Enter a number: "))
if num > 5:
    print(f"{num} is bigger than 5")
else:
    print(f"{num} is smaller than 5")

# 입력된 수가 짝수인지 홀수인지 검사
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
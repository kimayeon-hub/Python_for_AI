# ctrl + / : 한 번에 주석 처리/취소 가능

# input 함수는 string type으로 변수를 할당해줌
num = input("Enter a number: ")
print(f"type: {type(num)} / value: {num}")


# input()에서 할당 받은 변수 type casting하기
num = int(input("Enter a number: "))
print(f"type: {type(num)} / value: {num}")

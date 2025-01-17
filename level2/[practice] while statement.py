# n을 넘는 최초의 누적합
threshold_sum = int(input("Enter a number: "))

cum_sum = 0
i = 0
while cum_sum <= threshold_sum:
    cum_sum += i
    i += 1
    print(f"{i} - {cum_sum}")



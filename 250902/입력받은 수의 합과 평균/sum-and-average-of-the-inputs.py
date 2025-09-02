n = int(input())
li = [int(input()) for _ in range(n)]

sum_val = sum(li)
average_val = sum_val / len(li)
print(sum_val, round(average_val, 1))


n = int(input())
li = [int(input()) for _ in range(n)]

sum_val = 0
for num in li:
    if num % 2 == 1 and num % 3 == 0:
        sum_val += num
print(sum_val)

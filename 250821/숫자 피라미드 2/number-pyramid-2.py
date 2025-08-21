n = int(input())

sum_val = 0
for i in range(1, n+1):
    for j in range(i):
        sum_val += 1
        print(sum_val, end=' ')
    print()
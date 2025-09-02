li = [int(input()) for _ in range(10)]

num3 = 0
num5 = 0
for num in li:
    if num % 3 == 0:
        num3 += 1
    if num % 5 == 0:
        num5 += 1

print(num3, num5, end=' ')
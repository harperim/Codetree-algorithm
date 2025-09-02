li = [int(input()) for _ in range(10)]

cnt = 0
for num in li:
    if num % 2 == 1:
        cnt += 1
print(cnt)
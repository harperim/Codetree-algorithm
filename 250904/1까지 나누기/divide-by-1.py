n = int(input())

cnt = 0
for i in range(1, 100):
    if n > i:
        n /= i
        cnt += 1
    else:
        cnt += 1
        print(cnt)
        break

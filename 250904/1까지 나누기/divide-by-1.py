n = int(input())

cnt = 0
for i in range(1, n+1):
    if n > i:
        n /= i
        cnt += 1
    else:
        cnt += 1
        print(cnt)
        break

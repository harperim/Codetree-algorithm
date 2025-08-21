n = int(input())

for i in range(n):
    cnt = 1
    arr = []
    for j in range(n):
        arr.append(cnt)
        cnt += 1
    
    if i % 2 == 0:
        for j in range(n):
            print(arr[j], end='')
    else:
        for j in range(n-1, -1, -1):
            print(arr[j], end='')
    print()

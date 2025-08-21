start, end = map(int, input().split())

# Please write your code here.
answer = []
for num in range(start, end+1):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1

    if cnt == 3:
        answer.append(num)

print(len(answer))
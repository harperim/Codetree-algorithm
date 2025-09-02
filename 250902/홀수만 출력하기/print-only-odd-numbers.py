n = int(input())
li = [int(input()) for _ in range(n)]


for num in li:
    if num % 2 == 1 and num % 3 == 0:
        print(num)
n = int(input())
arr = list(map(int, input().split()))
even = []

for i in range(n):
    if arr[i] % 2 == 0:
        even.append(arr[i])

for i in range(len(even)-1, -1, -1):
    print(even[i], end=" ")

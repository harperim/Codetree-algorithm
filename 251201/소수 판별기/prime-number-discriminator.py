n = int(input())

li = []
for i in range(1, n+1):
    if n % i == 0:
        li.append(i)

if len(li) == 2 and li[-1] == n:
    print("P")
else:
    print("C")
n = int(input())

num_li = []
for i in range(1, n):
    if n % i == 0:
        num_li.append(i)

if sum(num_li) == n:
    print('P')
else:
    print('N')
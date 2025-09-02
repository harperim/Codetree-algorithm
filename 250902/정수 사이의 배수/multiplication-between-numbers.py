a, b = map(int, input().split())

num5 = []
num7 = []
for i in range(a, b+1):
    if i % 5 == 0:
        num5.append(i)
    if i % 7 == 0:
        num7.append(i)
sum_val = 0
sum_val = sum(num5) + sum(num7)
average_val = round(sum_val / (len(num5) + len(num7)), 1)
print(sum_val, average_val)
a, b = map(int, input().split())

sum_val = 0
if a > b:
    max_val = a
    min_val = b
else:
    max_val = b
    min_val = a

for i in range(min_val, max_val+1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)

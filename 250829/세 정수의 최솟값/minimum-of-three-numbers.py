a, b, c = map(int, input().split())

min_val = a

if min_val >= b:
    min_val = b
if min_val >= c:
    min_val = c

print(min_val)
a, b = map(int, input().split())

prod_val = 1
for _ in range(b):
    prod_val *= a
print(prod_val)

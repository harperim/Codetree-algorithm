a, b = map(int, input().split())

prod_val = 1
for i in range(1, b+1):
    if i % a == 0:
        prod_val *= i
print(prod_val)
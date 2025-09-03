n = int(input())

prod_val = 1
for i in range(1, 11):
    prod_val *= i
    if prod_val >= n:
        print(i)
        break
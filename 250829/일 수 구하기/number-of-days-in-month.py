n = int(input())

# 31 = 1 3 5 7 8 10 12 
# 30 = 2 4 6 9 11

if n == 2:
    print(28)
elif n >= 8:
    if n % 2 == 0:
        print(31)
    else:
        print(30)
else:
    if n % 2 == 0:
        print(30)
    else:
        print(31)
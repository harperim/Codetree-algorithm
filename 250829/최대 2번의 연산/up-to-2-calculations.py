n = int(input())

if n % 2 == 0:
    n //= 2

if n % 2 != 0:
    print((n+1) // 2)
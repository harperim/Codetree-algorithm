n = int(input())


# 6인 경우 3 / 12인 경우 12
classroom = 0
aisle = 0
bathroom = 0

for i in range(1, n+1):
    if i % 12 == 0:
        bathroom += 1
    elif i % 6 == 0 or i % 3 == 0:
        aisle += 1
    elif i % 2 == 0:
        classroom += 1

print(classroom, aisle, bathroom, end=' ')

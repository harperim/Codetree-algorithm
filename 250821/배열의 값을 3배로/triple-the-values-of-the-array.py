matrix = [list(map(int, input().split())) for _ in range(3)]

li = [
    [n * 3 for n in row]
    for row in matrix
]

for row in li:
    print(*row)


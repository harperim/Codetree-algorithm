rows, cols = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(rows)]
arr2 = [list(map(int, input().split())) for _ in range(rows)]

new_arr = []
for i in range(rows):
    new_rows = []
    for j in range(cols):
        if arr1[i][j] == arr2[i][j]:
            new_rows.append(0)
        else:
            new_rows.append(1)
    new_arr.append(new_rows)

for i in range(rows):
    print(*new_arr[i])

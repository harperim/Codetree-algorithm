arr1 = [list(map(int, input().split())) for _ in range(3)]
box = input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

new_arr = []
for i in range(3):
    new_row = []
    for j in range(3):
        new_row.append(arr1[i][j] * arr2[i][j])
    new_arr.append(new_row)

for i in range(3):
    print(*new_arr[i])

li = [int(input()) for _ in range(10)]

val_li = []
for num in li:
    if 0 <= num <= 200:
        val_li.append(num)

average_val = sum(val_li) / len(val_li)
print(sum(val_li), round(average_val, 1))
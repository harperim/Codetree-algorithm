li = ['apple', 'banana', 'grape', 'blueberry', 'orange']

letter = input()

answer = []
cnt = 0
for a in li:
    if a[2] == letter or a[3] == letter:
        answer.append(a)
        cnt += 1

for a in answer:
    print(a)
print(cnt)
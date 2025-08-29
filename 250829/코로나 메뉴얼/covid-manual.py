li = [input().split() for _ in range(3)]

sep = []

for i in range(3):
    li[i][1] = int(li[i][1])

for person in li:
    if person[0] == 'Y' and person[1] >= 37:
        sep.append('A')
    elif person[0] == 'N' and person[1] >= 37:
        sep.append('B')
    elif person[0] == 'Y':
        sep.append('C')
    else:
        sep.append('D')

cnt = 0
for s in sep:
    if s == 'A':
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')

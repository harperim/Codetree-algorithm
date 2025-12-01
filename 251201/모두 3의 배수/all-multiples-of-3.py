li  = [int(input()) for _ in range(5)]

cnt = 0
for i in range(len(li)):
    if li[i] % 3 == 0:
        cnt += 1

if cnt == len(li):
    print(1)
else:
    print(0)
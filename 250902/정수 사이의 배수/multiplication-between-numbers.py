a, b = map(int, input().split())

num_li = []
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        num_li.append(i)
   
sum_val = sum(num_li)
average_val = round(sum_val / (len(num_li)), 1)
print(sum_val, average_val)
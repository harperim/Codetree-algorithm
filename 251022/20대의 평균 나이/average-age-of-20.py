sum_val = 0
cnt_val = 0
while True:
    age = int(input())
    if age >= 30:
        break
    else:
        sum_val += age
        cnt_val += 1    

average = 0
if cnt_val != 0:
    average = sum_val / cnt_val
print(f"{average:.2f}")
    

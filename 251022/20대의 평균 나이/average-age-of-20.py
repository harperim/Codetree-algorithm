sum_val = 0
cnt_val = 0
while True:
    age = int(input())
    if age % 20 >= 10:
        break
    else:
        sum_val += age
        cnt_val += 1
    
if cnt_val == 0:
    print("입력된 값이 없습니다.")
else:
    average = "{:.2f}".format(sum_val / cnt_val)
    print(average)
    

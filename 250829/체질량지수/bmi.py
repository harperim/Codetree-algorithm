height, weight = map(int, input().split())

bmi = (10000*weight) // (height * height)
if bmi >= 25:
    print(bmi)
    print("Obesity")
else:
    print(bmi)
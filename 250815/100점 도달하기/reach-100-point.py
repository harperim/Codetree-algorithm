score = int(input())

while score <= 100:
    if score >= 90:
        print("A", end=" ")
        score += 1
    elif score >= 80:
        print("B", end=" ")
        score += 1
    elif score >= 70:
        print("C", end=" ")
        score += 1
    elif score >= 60:
        print("D", end=" ")
        score += 1
    else:
        print("F", end=" ")
        score += 1

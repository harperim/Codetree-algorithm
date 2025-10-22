

while True:
    width, length, letter = map(str, input().split())
    width, length = int(width), int(length)
    print(width * length)
    if letter == 'C':
        break
        
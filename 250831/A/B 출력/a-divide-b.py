a, b = map(int, input().split())

print(f'{a//b}.', end='')

a %= b
for _ in range(20):
    # 나머지에 10을 곱한 값을 기준으로
    # b로 나누었을 때의 몫 구하기
    a *= 10
    print(a//b, end="")
    
    a %= b
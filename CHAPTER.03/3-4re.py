# 답안 예시
n, k = map(int, input().split())
result = 0

while True:
    # n == k로 나누어떨어지는 수 가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 못 나눌 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빽
result += (n - 1)
print(result)
# 2가지 방식으로 구현한 팩토리얼 예제

# 1. 반복적으로 구현한 n!

def factorial_iterative(n):
    result = 1
    # 1 부터 n 까지의 수를 차례로 곱한다
    for i in range(1, n+1):
        result *= i
    return result

# 2. 재귀적으로 구현한 n!
    
def factorial_recursive(n):
    if n <= 1 : # n이 1 이하인 경우 1을 반환
        return 1

    # n! = n * (n-1)!
    return n * factorial_recursive(n-1)

# 각각 출력 
print('반복 : ', factorial_iterative(5))
print('재귀 : ', factorial_recursive(5))

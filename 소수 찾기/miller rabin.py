## overflow problem

def is_prime(n):
    i = 2
    while True:
        if i ** 2 > n:
            break
        elif n % i == 0:
             return False
        i += 1
    return True

def miller_rabin(n):
    alist = [2, 7, 61]
    d = n - 1
    s = 0
    while True:
        if d % 2 == 0:
            d /= 2
            s += 1
        else:
            break
    for a in alist:
        if  a ** d % n == 1:
            return False
            for j in range (s + 1):
                if a ** (d * 2 ** j) % n == -1:
                    return False
    return True

def solution(n):
    answer = 0
    for i in range (2, n + 1):
        if i <= 10000:
            if is_prime(i):
                answer += 1
        else:
            if miller_rabin(i):
                answer += 1
    return answer

print(solution(3984))




def fibonacci(n):
    answer = [0, 1]
    for i in range(n - 1):
        temp = sum(answer)
        del answer[0]
        answer.append(temp)
    return answer[1]

n = 5
print(fibonacci(n))

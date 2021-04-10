def failure_rate(N, stages):
    answer = []
    failure = []
    cnt = 0
    for i in range(1, N+1):
        if cnt != len(stages):
            failure.append((stages.count(i)/(len(stages) - cnt), i))
        else:
            failure.append((0, i))
        cnt += stages.count(i)
        
    failure = sorted(failure, key=lambda f:f[1])
    failure = sorted(failure, key=lambda f:f[0], reverse=True)
    for i in failure:
        answer.append(i[1])
    print(failure)
    
    return answer


N = 4
stages = [1, 1, 1, 1]
print(failure_rate(N, stages))


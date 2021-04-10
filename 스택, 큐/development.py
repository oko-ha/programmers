def development(progresses, speeds):
    answer = []
    while len(progresses):
        temp = 0
        while len(progresses):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                temp += 1
            else:
                break
        if temp > 0:
            answer.append(temp)
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

    return answer

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
        print(Q)
    return [q[1] for q in Q]

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))

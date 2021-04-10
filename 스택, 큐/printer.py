def printer(priorities, location):
    answer = 1
    while True:
        while priorities[0] != max(priorities):
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) -1
            else:
                location -= 1
        print(priorities)
        print(location)
        if location == 0:
            return answer
        else:
            priorities.pop(0)
            location -= 1
            answer += 1

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    print(queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))

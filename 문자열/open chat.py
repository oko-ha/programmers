def open_chat(record):
    result = []
    answer = []
    act = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    dic = {}
    for i in record:
        temp = i.split()
        print(temp) #
        if len(temp) > 2:
            dic[temp[1]] = temp[2]
        if temp[0] in act:
            result.append((temp[1], act[temp[0]]))
    print(dic) #
    print(result) #
    for i, j in result:
        answer.append(dic[i] + j)
    
    return answer

record = ["Enter uid1234 Muzi", \
          "Enter uid4567 Prodo", \
          "Leave uid1234", \
          "Enter uid1234 Prodo", \
          "Change uid4567 Ryan"]
print(open_chat(record))

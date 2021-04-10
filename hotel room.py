def hotel_room(k, room_number):
    answer = []
    num = [0] * (k + 1)
    m = -1
    j = [1, 1]

    for i in room_number:
        if num[i] == 0:
            num[i] = 1
            answer.append(i)
            if i > m:
                m = i
        else:
            # j 보다 상위
            if i > j[1]:
                try:
                    temp = num.index(0, i, m + 1)
                except:
                    j[0] = i
                    temp = m + 1
                    j[1] = temp

            # j 보다 하위
            elif i < j[0]:
                try:
                    temp = num.index(0, i, j[0] + 1)
                except:
                    j[0] = i
                    temp = j[1] + 1
                    j[1] = temp

            # j 가운데 범위
            else:
                try:
                    temp = num.index(0, j[1], m + 1)
                except:
                    temp = m + 1
                    j[1] = temp
                    
            num[temp] = 1
            answer.append(temp)
            if temp > m:
                m = temp
        print(j)
        print(num)
            
    return answer

k = 15
room_number = [2, 1, 5, 6, 8, 6, 1, 6]#, 1, 6, 11, 5, 11]
print(hotel_room(k, room_number))

def hotel_room(k, room_number):
    answer = []
    temp = [1, 2, 3, 4, 5]
    room_left = {}
    room_in = {}
    for i in range(1, k+1):
        room_left[i] = i

    for i in room_number:
        if i in room_left:
            room_in[i] = 1
            answer.append(room_left.pop(i))
        else:
            for j in range(i, 
            answer.append(hash_map.pop())
            
    return answer

k = 15
room_number = [4, 5, 7, 9, 10] #, 1, 6, 11, 5, 11]
print(hotel_room(k, room_number))

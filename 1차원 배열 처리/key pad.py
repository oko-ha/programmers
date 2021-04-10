def key_pad(numbers, hand):
    conf = {1:'L', 3:'R', 4:'L', 6:'R', 7:'L', 9:'R'}
    pos = {1:0, 2:0, 3:0, 4:1, 5:1, 6:1, 7:2, 8:2, 9:2, 0:3}
    hands = {"left":'L', "right":'R'}
    pos_l = pos_r = 3
    mid_l = mid_r = 1
    answer = ''
    for i in numbers:
        if i in [2, 5, 8, 0]:
            if abs(pos_l - pos[i]) + mid_l < abs(pos_r - pos[i]) + mid_r:
                answer += 'L'
            elif abs(pos_l - pos[i]) + mid_l > abs(pos_r - pos[i]) + mid_r:
                answer += 'R'
            else:
                answer += hands[hand]
            mid = 0
        else:
            answer += conf[i]
            mid = 1
        if answer[-1] == 'L':
            mid_l = mid
            pos_l = pos[i]
        else:
            mid_r = mid
            pos_r = pos[i]

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(key_pad(numbers, hand))

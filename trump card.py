import random
import re
import copy

def game(pick):
    plist = re.findall('([SDHC])(\w\d?)', pick)
    print(plist)

    n_dict = {'A' : '14', 'J' : '11', 'Q' : '12', 'K' : '13'}
    p_number = []
    p_shape = []
    for i in range(len(plist)):    
        p_shape.append(plist[i][0])
        if plist[i][1].isdigit():
            p_number.append(int(plist[i][1]))
        else:
            p_number.append(int(n_dict[plist[i][1]]))

    # Pair, Triple, FullHouse, Fourcard
    # Pair : 2
    # Two Pair : 22
    # Triple : 3
    # FullHouse : 23 or 32
    # Fourcard : 4
    temp = copy.deepcopy(p_number)
    s_temp = list(set(temp))
    cnt = ''
    for i in range(len(s_temp)):
        if temp.count(s_temp[i]) > 1:
            cnt += str(temp.count(s_temp[i]))

    # Straight
    # sFlag { 0: None, 1: Straight, 2: Back, 3: Mountain }
    sFlag = 0
    temp.sort()
    print(temp)
    if temp[-1] - temp[0] == 4:
        sFlag = 1
        if temp[-1] == 14:
            sFlag = 3
    elif temp[-1] - temp[-2] == 9:
        sFlag = 2

    # Flush
    fFlag = False
    p_shape = set(p_shape)
    if len(p_shape) == 1:
        fFlag = True
    
    # Result
    if cnt == '4':
        result = 9
    elif cnt == '23' or cnt == '32':
        result = 8
    elif cnt == '3':
        result = 3
    elif cnt == '22':
        result = 2
    elif cnt == '2':
        result = 1
    elif fFlag:
        if sFlag == 3:
            result = 12
        elif sFlag == 2:
            result = 11
        elif sFlag == 1:
            result = 10
        else:
            result = 7
    elif sFlag > 0:
        if sFlag == 3:
            result = 6
        elif sFlag == 2:
            result = 5
        else:
            result = 4
    else:
        result = 0
    
    return result

# Card shuffle
def game_start(card):
    for i in range(random.randrange(1, 6)):
        random.shuffle(card)

    pick = ''
    for i in range(0, 5):
        pick += card[i]

    return pick

## S : ♠, D : ◆, H : ♥, C : ♣
shape = ['S', 'D', 'H', 'C']
## number : 2 - 10, J, Q, K, A
number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card = []
for i in range(len(shape)):
    for j in range(len(number)):
        card.append(shape[i] + number[j])

point = { 0 : 'Top', \
          1 : 'One Pair', \
          2 : 'Two Pair', \
          3 : 'Triple', \
          4 : 'Straight', \
          5 : 'Back Straight', \
          6 : 'Mountain', \
          7 : 'Flush', \
          8 : 'Full house', \
          9 : 'Four card', \
          10 : 'Straight Flush', \
          11 : 'Back Straight Flush',
          12 : 'Royal Straight Flush'
    }
lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while True:
    pick = game_start(card)
    n = game(pick)
    lst[n] += 1
    print(point[n])
    i += 1
    if i == 500:
        break
print(i, '번 시도했음ㅋㅎ')
print(lst)
for x in range(len(lst)):
    print(point[x], ':', lst[x]/i * 100, '%')

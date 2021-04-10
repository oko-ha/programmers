def base_N(n, t, m, p):
    base = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    temp = '0'
    i = 0
    answer = ''
    while len(temp) <= t * m:
        x = ''
        i += 1
        num = i
        while num > 0:
            if num % n > 9:
                x = base[num%n] + x
            else:
                x = str(num%n) + x
            num //= n
        temp += x
    answer = temp[p-1::m][:t]
        
    return answer

cond = [16, 16, 2, 2]
print(base_N(cond[0], cond[1], cond[2], cond[3]))

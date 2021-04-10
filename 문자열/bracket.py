def bracket(s):
    from collections import Counter
    map = Counter(s)
    lst = [i for i in s]
    if map['('] != map[')']:
        return False

    left = 0
    right = 0
    for i in lst:
        if i == '(':
            left += 1
        else:
            right += 1
        if left - right < 0:
            return False

    return True



s = "(())(())"
print(bracket(s))

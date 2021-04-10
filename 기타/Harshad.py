def harshad(x):
    return x % sum([int(i) for i in str(x)]) == 0

x = 18
print(harshad(x))

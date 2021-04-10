import itertools
from collections import Counter
def prime(nums):
    answer = Counter([sum(i) for i in itertools.combinations(nums,3)])
    for i in range(2, int(max(answer)**0.5)+1):
        if not answer:
            return 0
        for j in range(i*i, max(answer)+1, i):
            del answer[j] 
    return sum(answer.values())


nums = [1, 2, 4, 5, 7, 8]
print(prime(nums))

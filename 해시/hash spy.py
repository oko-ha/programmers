from collections import Counter
def spy(clothes):
    answer = 1
    for i in Counter([i[1] for i in clothes]).values():
        answer *= (i + 1)

    return answer - 1

clothes = [["yellowhat", "headgear"],\
           ["bluesunglasses", "eyewear"],\
           ["brownlens", "eyewear"], \
           ["green_turban", "headgear"], \
           ["cheapsunglasses", "eyewear"], \
           ["crowmask", "face"]]
print(spy(clothes))

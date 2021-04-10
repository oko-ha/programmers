def word_chain(n, words):
    temp = ''
    dic = {}
    i = 0
    for word in words:
        if temp:
            if temp[-1] != word[0]:
                return [i%n+1, i//n+1]
        if word in dic:
            return [i%n+1, i//n+1]
        temp = word
        dic[word] = 1
        i += 1

    return [0, 0]

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]

print(word_chain(n, words))

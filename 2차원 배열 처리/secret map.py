def secret_map(n, arr1, arr2):
    decode = {'0':' ', '1':'#'}
    answer = []
    for i, j in zip(arr1, arr2):
        answer.append(''.join([decode[x] for x in format(i | j, 'b').zfill(n)]))
    
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(secret_map(n, arr1, arr2))

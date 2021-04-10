import re

def solution(new_id):
    #1 대문자 -> 소문자 치환
    answer = new_id.lower()

    #2 특수문자 제거
    special_char = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']
    for s_char in special_char:
        answer = answer.replace(s_char,'')

    #3 마침표 중복 제거
    answer = re.sub('[.]+', '.', answer)

    #4 마침표 처음 끝 제거
    if answer.find('.') == 0:
        answer = answer[1:]
    if answer.rfind('.') == len(answer) - 1:
        answer = answer[:-1]

    #5 빈 문자열일 때
    if len(answer) == 0:
        answer = 'a'

    #6 길이가 16자 이상일 때
    if len(answer) >= 16:
        answer = answer[:15]

    if answer.find('.') == 0:
        answer = answer[1:]
    if answer.rfind('.') == len(answer) - 1:
        answer = answer[:-1]

    #7 길이가 2자 이하일 때
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer

print(solution('z-+.^.'))

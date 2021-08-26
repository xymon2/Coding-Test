#https://programmers.co.kr/learn/courses/30/lessons/42577
# startswith, endswith 없엇으면 어케풀었을까

def solution(phone_book):
    phone_book.sort()
    answer = True

    for i in range(len(phone_book) - 1):
        a = phone_book[i]
        b = phone_book[i + 1]
        if b.startswith(a):
            return False

    return answer

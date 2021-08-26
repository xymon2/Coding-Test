#https://programmers.co.kr/learn/courses/30/lessons/42584

#list에서 deque로 바꿨을 뿐인데 효율성통과가 됐다 ㄷ ㄷ

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices) != 0:
        a = prices.popleft()
        count = 0
        for item in prices:
            if item < a:
                count += 1
                break
            else:
                count += 1
        answer.append(count)

    return answer
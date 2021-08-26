#https://programmers.co.kr/learn/courses/30/lessons/72411
#is subset 생각한게 신의 한수

from itertools import combinations

def solution(orders, course):
    answer = set()
    mm = {}

    crs = {}
    for orde in orders:
        o = list(orde)
        for k in course:
            a = set(combinations(o, k))
            if crs.get(k) == None:
                crs[k] = a
            else:
                crs[k] = crs[k] | a

    for k in course:
        a = crs[k]
        count = []

        for cours in a:
            c = set(cours)
            cnt = 0
            for order in orders:
                if c.issubset(order):
                    cnt += 1
            if cnt > 1:
                count.append([cnt, cours])

        if count:
            a = max(count)
            for item in count:
                if item[0] == a[0]:
                    b = list(item[1])
                    b.sort()
                    answer.add(''.join(b))

    answer = list(answer)
    answer.sort()
    return answer
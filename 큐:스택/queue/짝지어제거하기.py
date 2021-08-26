#https://programmers.co.kr/learn/courses/30/lessons/12973#
#re 보다 빠르네

from collections import deque

def solution(s):
    stac = []
    stlist = deque(list(s))

    for i in range(len(stlist)):
        new = stlist.popleft()
        if len(stac) != 0 and new == stac[-1]:
            stac.pop()
        else:
            stac.append(new)

    if len(stac) == 0:
        return 1
    else:
        return 0

    # while True:
    #     new = re.sub('((.)\\2{1})', '', s)
    #     print(new,s)
    #     if new == s:
    #         break
    #     else:
    #         s = new

    # if len(s) == 0:
    #     return 1
    # else:
    #     return 0

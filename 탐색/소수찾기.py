#https://programmers.co.kr/learn/courses/30/lessons/42839#
# 너무 복잡한데...더 간단한풀이 있을라나
# 이정도면 양호한듯?

from itertools import permutations

def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, a):
        if (a % i == 0):
            return False
    return True


def tup_to_string(tup):
    ans = ""
    for num in tup:
        ans += str(num)
    return ans


def solution(numbers):
    n = []
    new_list = []
    perm = set()

    for i in numbers:
        n.append(int(i))

    for i in range(len(n) + 1):
        a = list(permutations(n, i))
        new_list.extend(a)

    for tup in new_list:
        if len(tup) != 0:
            num = int(tup_to_string(tup))
            perm.add(num)

    answer = 0

    for num in perm:
        if isPrime(num):
            answer += 1

    return answer
#https://programmers.co.kr/learn/courses/30/lessons/60058
#지렷노

def valid(p_list: list) -> bool:
    pop_list = []

    while p_list:
        p = p_list.pop()

        if p == '(':
            if pop_list and pop_list[-1] == ')':
                pop_list.pop()
                continue

        pop_list.append(p)

    if pop_list:
        return False
    else:
        return True


def balanced(p):
    left = 0
    right = 0
    rest = []
    while p:
        paren = p.pop(0)
        if paren == '(':
            left += 1
        else:
            right += 1
        rest.append(paren)
        if left == right:
            break
    return rest, p



def recur(p):
    ans = []
    if len(p) == 0:
        return []
    u, v = balanced(p)
    if valid(u[:]):
        ans.extend(u)
        ans.extend(recur(v))
    else:
        ans.append('(')
        a = recur(v)
        ans.extend(a)
        ans.append(')')
        u.pop()
        u.pop(0)
        for idx in range(len(u)):
            if u[idx] == '(':
                u[idx] = ')'
            else:
                u[idx] = '('
        ans.extend(u)
    return ans


def solution(p):
    answer = ''

    if len(p) == 0:
        return ''
    if valid(list(p)):
        return p

    a = recur(list(p))
    answer = ''.join(a)

    return answer
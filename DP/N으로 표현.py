#https://programmers.co.kr/learn/courses/30/lessons/42895
#어벙한실수로 한참 해맸다.


def solution(N, number):
    if N == number:
        return 1

    a = [0, [N]]

    for i in range(2, 9):
        b = {int(str(N) * i)}
        for half in range(1, i // 2 + 1):
            for num1 in a[half]:
                for num2 in a[i - half]:
                    b.add(num1 + num2)
                    b.add(num1 - num2)
                    b.add(num2 - num1)
                    b.add(num1 * num2)
                    if num1 != 0:
                        b.add(num2 // num1)
                    if num2 != 0:
                        b.add(num1 // num2)
            if number in b:
                return i

        a.append(b)

    return -1
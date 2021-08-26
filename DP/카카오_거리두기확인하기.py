#https://programmers.co.kr/learn/courses/30/lessons/81302#fn1
#복잡하긴했는데 쉬웠다.
#그때그때 검사하는거보다 좌표를 배열에 저장하는게 훨 낫네.


def solution(places):
    answer = []

    for room in places:
        Pcord = []
        Ocord = []
        for y, line in enumerate(room):
            for x, place in enumerate(line):
                if place == 'P':
                    Pcord.append([x, y])
                elif place == 'O':
                    Ocord.append([x, y])
        cnt = 1
        for item in Pcord:
            if [item[0] + 1, item[1]] in Pcord or [item[0], item[1] + 1] in Pcord:
                cnt = 0
                answer.append(0)
                break

            elif [item[0] + 2, item[1]] in Pcord:
                if [item[0] + 1, item[1]] in Ocord:
                    cnt = 0
                    answer.append(0)
                    break

            elif [item[0], item[1] + 2] in Pcord:
                if [item[0], item[1] + 1] in Ocord:
                    cnt = 0
                    answer.append(0)
                    break

            elif [item[0] - 1, item[1] + 1] in Pcord:
                if [item[0] - 1, item[1]] in Ocord or [item[0], item[1] + 1] in Ocord:
                    cnt = 0
                    answer.append(0)
                    break

            elif [item[0] + 1, item[1] + 1] in Pcord:
                if [item[0] + 1, item[1]] in Ocord or [item[0], item[1] + 1] in Ocord:
                    cnt = 0
                    answer.append(0)
                    break
        if cnt == 1:
            answer.append(1)

    return answer
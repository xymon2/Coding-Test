#https://programmers.co.kr/learn/courses/30/lessons/64061
#이정도는 쉽지


def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in board:
            if j[i - 1] == 0:
                continue

            else:
                basket.append(j[i - 1])
                j[i - 1] = 0
                break
        # print(basket)
        if len(basket) > 1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2

    return answer
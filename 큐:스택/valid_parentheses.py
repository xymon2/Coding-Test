#https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:

        p_list = list(s)
        pop_list = []

        while p_list:
            p = p_list.pop()

            if p == '(':
                if pop_list and pop_list[-1] == ')':
                    pop_list.pop()
                    continue
            elif p == '{':
                if pop_list and pop_list[-1] == '}':
                    pop_list.pop()
                    continue
            elif p == '[':
                if pop_list and pop_list[-1] == ']':
                    pop_list.pop()
                    continue

            pop_list.append(p)

        # print(pop_list)
        if pop_list:
            return False
        else:
            return True

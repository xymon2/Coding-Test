#https://leetcode.com/problems/reverse-linked-list-ii/submissions/
#만약 결과가 잘린다면 이것처럼 하나 더 지정해보자
#씨발..

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        node = head
        root = prev = ListNode(None)
        root.next = head

        for i in range(left - 1):
            prev = node
            node = node.next

        for i in range(right - left):
            nxt = node.next
            node.next = node.next.next
            nxt.next = prev.next
            prev.next = nxt

        return root.next

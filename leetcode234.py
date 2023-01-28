# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
        l = []
        def unpack(x: ListNode):
            l.append(x.value)
            if x.next:
                return unpack(x.next)
            else:
                return

        n = len(l) // 2
        return l[:n] == l[-1:-n - 1:-1]

def test():
    isPalindrome(ListNode(2,ListNode(1)))
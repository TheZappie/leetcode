from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def unwrap_recursive(ll: ListNode):
    if ll.next:
        return str(ll.val) + unwrap(ll.next)
    else:
        return str(ll.val)

def wrap_recursive(n: str):
    if n:
        return ListNode(n[0], wrap(n[1:]))
    else:
        return


def unwrap(ll: ListNode):
    result = []
    current_node = ll
    while True:
        result.append(current_node.val)
        if current_node.next:
            current_node = current_node.next
        else:
            break
    return ''.join(map(str, reversed(result)))


def wrap(string: str):
    last_node = ListNode(string[0], None)
    for s in string[1:]:
        last_node = ListNode(s, last_node)
    return last_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number = int(unwrap(l1)) + int(unwrap(l2))
        return wrap(str(number))

# Solution().addTwoNumbers(wrap('243'), wrap('564'))

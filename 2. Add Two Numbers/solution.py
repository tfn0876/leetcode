# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoNumbersWithBorrow(l1, l2, 0)

    def addTwoNumbersWithBorrow(self, l1, l2, borrow):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            if borrow > 0:
                return ListNode(borrow)
            else:
                return None
        elif l1 is None:
            l = ListNode((l2.val + borrow) % 10)
            l.next = self.addTwoNumbersWithBorrow(
                None, l2.next, (l2.val + borrow) // 10)
            return l
        elif l2 is None:
            l = ListNode((l1.val + borrow) % 10)
            l.next = self.addTwoNumbersWithBorrow(
                l1.next, None, (l1.val + borrow) // 10)
            return l
        l = ListNode((l1.val + l2.val + borrow) % 10)
        l.next = self.addTwoNumbersWithBorrow(
            l1.next, l2.next, (l1.val + l2.val + borrow) // 10)
        return l

    def createList(self, array1, index):
        if index < len(array1):
            l = ListNode(array1[index])
            l.next = self.createList(array1, index + 1)
            return l
        else:
            return None

    def printList(self, l):
        """
        :type l: ListNode
        """
        if l is not None:
            print(l.val)
            self.printList(l.next)


# Run Test
l1 = Solution().createList([2, 4, 3], 0)
l2 = Solution().createList([5, 6, 4], 0)
l = Solution().addTwoNumbers(l1, l2)
Solution().printList(l)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # def rev_num(head):
        #     num = 0
        #     mul = 1

        #     while head:
        #         num += head.val * mul
        #         mul  *= 10
        #         head = head.next
        #     return num
        
        # n1 = rev_num(l1)               <----------- very slow solution therefor below is a optimized solution
        # n2 = rev_num(l2)
        # total = n1 + n2

        # if total == 0:
        #     return ListNode(0)

        # dummy = ListNode(0)
        # curr = dummy

        # while total > 0 :
        #     digit =  total % 10
        #     curr.next = ListNode(digit)
        #     curr = curr.next
        #     total = total // 10

        # return dummy.next


        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            temp_sum_val = carry + val1 + val2
            sum_val = temp_sum_val % 10
            carry = temp_sum_val // 10
            

            curr.next = ListNode(sum_val)
            curr = curr.next

            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None
        return dummy.next





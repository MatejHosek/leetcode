class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        end = None

        carry = 0
        while (l1 is not None or l2 is not None) or carry != 0:
            # Calculate the sum of next two nodes
            sum = 0
            sum += carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next

            # Calculate the carry and update sum
            carry = (sum - (sum % 10)) // 10
            sum = sum % 10

            if head is None:
                head = ListNode(sum, None)
                end = head
                continue

            end.next = ListNode(sum, None)
            end = end.next
        return head

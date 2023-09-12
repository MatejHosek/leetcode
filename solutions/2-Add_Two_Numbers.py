class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits = []

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

            digits.append(sum)

        # Loop through list nodes and construct linked list
        solution = None; i = len(digits) - 1
        while i >= 0:
            solution = ListNode(digits[i], solution)
            i -= 1

        return solution

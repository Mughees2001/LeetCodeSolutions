# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        k = k % sizeList(head)
        if k == 0:
            print("Returning Head:",head)
            return head
        else:
            tempNode = head
            newHead = None
            while tempNode.next.next is not None:
                tempNode = tempNode.next
            newHead = tempNode.next
            tempNode.next = None
            newHead.next = head
            return self.rotateRight(newHead,k-1)

def sizeList(head):
        count = 0
        while head is not None:
            count +=1
            head = head.next
        return count
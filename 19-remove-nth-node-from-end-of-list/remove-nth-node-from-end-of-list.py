# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def sizeList(head):
    count = 0
    while head is not None:
        head = head.next
        count+=1
    return count


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        print("Size of list:",sizeList(head))
        removeIndex = sizeList(head) - n
        if removeIndex == 0:
            head = head.next
            return head
        else:
            count = 0
            tempNode = head
            deleteNode = head.next
            while count < removeIndex - 1:
                count+=1
                tempNode = tempNode.next
                deleteNode = deleteNode.next
            tempNode.next = deleteNode.next
            deleteNode = None
            return head




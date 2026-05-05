class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find length
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

   
    tail.next = head

   
    k = k % length
    steps_to_new_head = length - k

    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next

    new_head = new_tail.next

    new_tail.next = None

    return new_head


values = list(map(int, input("Enter linked list values (space separated): ").split()))
k = int(input("Enter k (number of rotations): "))

dummy = ListNode(0)
current = dummy
for val in values:
    current.next = ListNode(val)
    current = current.next

head = dummy.next

new_head = rotateRight(head, k)


print("Rotated List:")
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next

#sample input:
# Enter linked list values (space separated): 1 2 3 4 5
# Enter k (number of rotations): 2
# Rotated List:
# 4 5 1 2 3
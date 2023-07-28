class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

head = Node('AAAAA - 55', Node('MMMMMM - 18', Node('AAAAA - 22', Node('CCCCC - 44', Node('AAAAA - 45', Node('FFFF - 34'))))))

def print_list(head, end='\n'):
    while head:
        print(head.data, end=';\t' if head.next else '')
        head = head.next
    print(end=end)

print_list(head)

def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

print_list(reverse_list(head))
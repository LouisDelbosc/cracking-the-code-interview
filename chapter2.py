from linked_list import Node

""" Remove dups
Write code to remove duplicate from an unsorted linked list
How would you solve this problem if a temporary buffer isn't allowed ?
"""

def remove_duplicate(head):
    dups = {}
    curr, prev = head, None
    while curr != None:
        if dups.get(curr.data, False) == False:
            dups[curr.data] = True
            prev = curr
        else:
            prev.next = curr.next
        curr = curr.next
    return head

head = Node(5)
head.append_array([2, 3, 4, 2, 3, 4])
print "remove duplicate [5, 2, 3, 4, 2, 3, 4]", remove_duplicate(head).to_list() == [5, 2, 3, 4]

""" Return kth to last
Implement an algorithm to find the kth to last element of a singly linked list
"""

def kth_to_last(head, k):
    if k == 0:
        return Node(None)
    first, second = head, head
    while k > 0:
        k -= 1
        first = first.next
    while first != None:
        first, second = first.next, second.next
    return second

head = Node(10)
head.append_array([9,8,4,3,2,1])
print "3rd to last of [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]", kth_to_last(head, 3).data == 3
print "0th to last of [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]", kth_to_last(head, 0).data == None

""" Delete middle node
Implement a algorithm to delete a node in the middle (not first nor last) of a single linked list given only access to that node
"""

def delete_middle_node(middle):
    middle.data = middle.next.data
    middle.next = middle.next.next

head = Node(5)
middle = Node(10)
head.append_array([1, 2, 3])
middle.append_array([3, 2, 1])
head.append_node(middle)
delete_middle_node(middle)
print head.to_list() == [5, 1, 2, 3, 3, 2, 1]

""" Partition
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater or equal to x.
If x is contained within the list, the value of x the value of x only need to be after the element less than x. The partition element x can appear anywhere in the right partition; it does not need to appear between the left and the right partitions.
Example:
[input] [3, 5, 8, 5, 10, 2, 1] partition 5
[output] [3, 1, 2, 10, 5, 5, 8]
"""

""" Sum Lists
You have two numbers represented by a libnked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
Example:
[7, 1, 6] + [5, 9, 2] => [2, 1, 9]

Suppose the digits are stored in forward order. Repeat the above problem
Example:
[6, 1, 7] + [3, 2, 9, 5] => [3, 9, 1, 2]
"""

def sum_list1(h1, h2):
    acc = 0
    res = None
    c1, c2 = h1, h2
    while c1 != None or c2 != None:
        if c1 != None:
            v1 = c1.data
            c1 = c1.next
        else:
            v1 = 0
        if c2 != None:
            v2 = c2.data
            c2 = c2.next
        else:
            v2 = 0
        val = v1 + v2 + acc
        tmp = val % 10
        acc = val / 10
        if res:
            res.append(tmp)
        else:
            res = Node(tmp)
    if acc != 0:
        res.append(acc)
    return res

h1, h2 = Node(7), Node(5)
h1.append_array([1, 6])
h2.append_array([9, 3])
print "sum list 1", sum_list1(h1, h2).to_list() == [2, 1, 0, 1]

def pad_list(h1, h2):
    c1, c2 = h1, h2
    l1, l2 = 0,0
    while c1 != None:
        l1 += 1
        c1 = c1.next
    while c2 != None:
        l2 += 1
        c2 = c2.next

    if l1 < l2:
        h = Node(0)
        padding = [0 for _ in xrange(l1 - l2 - 1)]
        h.append_array(padding)
        h.append_node(h1)
        return h, h2
    elif l1 > l2:
        h = Node(0)
        padding = [0 for _ in xrange(l2 - l1 - 1)]
        h.append_array(padding)
        h.append_node(h2)
        return h1, h
    else:
        return h1, h2

def deep_sum(h1, h2):
    if h1.next == None and h2.next == None:
        val = (h1.data + h2.data) % 10
        acc = (h1.data + h2.data) / 10
        return Node(val), acc
    else:
        node, acc = deep_sum(h1.next, h2.next)
        val = h1.data + h2.data + acc
        tmp, acc = val % 10, val / 10
        n = Node(tmp)
        n.append_node(node)
        return n, acc

def sum_list2(h1, h2):
    h1, h2 = pad_list(h1, h2)
    node, acc = deep_sum(h1, h2)
    if acc != 0:
        n = Node(acc)
        n.append_node(node)
        node = n
    return node

h1, h2 = Node(9), Node(6)
h1.append_array([4, 7, 4])
h2.append_array([9, 5])
print "sum list 2", sum_list2(h1, h2).to_list() == [1, 0, 1, 6, 9]


""" Palindrome
Implement a function to check if a linked list is a palindrome.
"""

def reverse(node):
    n = node
    tmp = []
    while n.next != None:
        tmp.append(n.data)
        n = n.next
    tmp.append(n.data)

    copy_node = Node(tmp[-1])
    curr = copy_node
    for i in xrange(1, len(tmp)):
        curr.next = Node(tmp[-i-1])
        curr = curr.next
    return copy_node

def palindrome(head):
    tail = reverse(head)
    print tail.to_list(), head.to_list()
    curr1, curr2 = head, tail
    while curr1 != None:
        if curr1.data != curr2.data:
            return False
        curr1, curr2 = curr1.next, curr2.next
    return True

head = Node(5)
head.append_array([3,2,1,2,3,5])
print "palindrome", palindrome(head) == True


""" Intersection
Given two singly linked list, determine if the two lists intersect.
Return the intersecting node.
"""

def intersection(h1, h2):
    first, second = {}, {}
    c1, c2 = h1, h2
    while c1.next != None or c2.next != None:

        if c1.next != None:
            first[c1] = True
            if second.get(c1, False):
                return c1
            c1 = c1.next

        if c2.next != None:
            second[c2] = True
            if first.get(c2, False):
                return c2
            c2 = c2.next
    return False

""" Loop detection
Given a circular linked list, implement an algorithm that returns the node at the begining of the loop.
"""

def loop_detection(head):
    check = {}
    curr = head
    while curr.next != None:
        if check.get(curr, False) == False:
            check[curr] = True
        else:
            res = curr
            break
        curr = curr.next
    return res

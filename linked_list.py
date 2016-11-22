class Node():
    def __init__(self, value, nextNode=None):
        self.data = value
        self.next = nextNode

    def append(self, value):
        n = self
        while n.next != None:
            n = n.next
        n.next = Node(value)

    def append_array(self, array):
        for elem in array:
            self.append(elem)

    def append_node(self, node):
        n = self
        while n.next != None:
            n = n.next
        n.next = node

    def to_list(self):
        res = []
        curr = self
        while curr != None:
            res.append(curr.data)
            curr = curr.next
        return res

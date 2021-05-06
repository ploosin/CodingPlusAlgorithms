class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class DoubleLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = self.head

    def add(self, node):
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insert_before(self, node, before_node):
        if self.head == None:
            self.head = node
            return 
        else:
            cur = self.tail
            while cur.data != before_node.data:
                cur = cur.prev
                if cur == None:
                    return
            node.next = cur
            prev_node = cur.prev
            node.prev = prev_node
            cur.prev = node
            if prev_node == None:
                self.head = node
            else:
                prev_node.next = node
            

    def insert_after():
        pass

    def delete(self, node):
        find = False
        if self.head: 
            cur = self.head
            if cur.data == node.data:
                find = True
                if cur.next:
                    self.head = cur.next
                    self.head.prev = None
                else:
                    self.head = None
                print('Delete:', cur)
                del cur
            else:
                while cur.next:
                    if cur.next.data == node.data:
                        find = True
                        tmp = cur.next
                        if cur.next.next != None:       # if cur.next is not tail
                            cur.next.next.prev = cur
                        else:                           # if cur.next is tail
                            self.tail = cur
                        cur.next = cur.next.next
                        print('Delete:', tmp)
                        del tmp
                        break
                    else:
                        cur = cur.next
            if self.tail == None:
                    self.tail = self.head
            if not find:
                print('Not Exist Node:', node)
        else:
            print('Empty Node')

    def search(self, node):
        cur = self.head
        while cur:
            if cur.data == node.data:
                print('search:', node)
                return
            else:
                cur = cur.next
        print('Not Exist Node:', node)

    def print(self):
        if self.head == None:
            print('Empty Node')
        else:
            cur = self.head
            while cur:
                print(cur.data)
                cur = cur.next

    def print_from_tail(self):
        if self.tail == None:
            print('Empty Node')
        else:
            cur = self.tail
            while cur:
                print(cur.data)
                cur = cur.prev


dll = DoubleLinkedList(Node(10))
dll.add(Node(100))
dll.add(Node(1000))
dll.print()

dll.delete(Node(100))

dll.print()
dll.delete(Node(1000))
dll.print()
dll.delete(Node(1000))
dll.print()

dll.search(Node(10))
dll.search(Node(1000))

dll.add(Node(50))
dll.add(Node(5000))
dll.print()

dll.delete(Node(10))
dll.delete(Node(5000))
dll.print()
dll.delete(Node(50))
dll.print()

dll.add(Node(99))
dll.add(Node(999))
dll.print()

dll.print_from_tail()
print('---------------------')
dll.insert_before(Node(888), Node(999))
dll.print()
print('---------------------')
dll.insert_before(Node(88), Node(99))
dll.print()

print('---------------------')
dll.insert_before(Node(777), Node(888))
dll.print()
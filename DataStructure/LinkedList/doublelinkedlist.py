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
            self.head = self.node
            self.tail = self.head
        else:
            # self.tail.next = node
            # node.prev = self.tail
            # self.tail = node
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur
            self.tail = node

            # node.prev = self.tail
            # self.tail.next = node
            # self.tail = node

    def delete(self, node):
        find = False
        if self.head:
            cur = self.head
            if cur.data == node.data:
                self.head = cur.next
                self.head.prev = None
                del cur
            else:
                while cur.next:
                    if cur.next.data == node.data:
                        find = True
                        tmp = cur.next
                        if cur.next.next != None:
                            cur.next.next.prev = cur
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


sll = DoubleLinkedList(Node(10))
sll.add(Node(100))
sll.add(Node(1000))
sll.print()

sll.delete(Node(100))

sll.print()
sll.delete(Node(1000))
sll.print()
sll.delete(Node(1000))
sll.print()

sll.search(Node(10))
sll.search(Node(1000))

sll.add(Node(50))
sll.add(Node(5000))
sll.print()
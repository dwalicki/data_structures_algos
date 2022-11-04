class Node(object):
    def __init__(self, d):
        self.next_node = None
        self.d = d


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, d):
        new_node = Node(d)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def add_at(self, d, index):
        new_node = Node(d)
        previous_node = None
        current_node = self.head
        i = 0
        while i < index and current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
            i += 1
        if i == index:
            previous_node.next_node = new_node
            new_node.next_next = current_node
            return True
        else:
            return False

    def remove(self, d):
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == d:
                if previous_node:
                    previous_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node
                self.size -= 1
                return True
            previous_node = current_node
            current_node = current_node.next_node
        return False

    def find(self, d):
        current_node = self.head
        while current_node:
            if current_node.data == d:
                return True
            current_node = current_node.next_node
        return False

    def to_list(self):
        l = []
        current_node = self.head
        while current_node:
            l.append(current_node.data)
            current_node = current_node.next_node
        return l
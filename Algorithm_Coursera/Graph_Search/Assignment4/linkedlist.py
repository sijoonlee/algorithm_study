class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.first = None
        self.length = 0
    
    def len(self):
        return self.length

    def add(self, value): # de-duplicate
        if self.first is None:
            self.first = Node(value)
            self.length += 1
        else:
            walker = self.first
            duplicate = False
            while walker is not None:
                if walker.value == value:
                    duplicate = True
                    break
                if walker.next is None:
                    break
                walker = walker.next
            if not duplicate:
                walker.next = Node(value)
                self.length += 1
    
    def lookup(self, value):
        walker = self.first
        found = False
        while walker is not None:
            if walker.value == value:
                found = True
                break
            walker = walker.next
        return found
    
    def print(self):
        walker = self.first
        print("len", self.length)
        while walker is not None:
            print(walker.value)
            walker = walker.next



if __name__ == "__main__":
    test = LinkedList()
    test.add(1)
    test.print()
    test.add(2)
    test.print()
    test.add(3)
    test.print()
    test.add(3)
    test.print()
    test.add(1)
    test.print()
    print(test.lookup(3))
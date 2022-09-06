import node

class LinkedList:

    def __init__(self, first):
        self.first = first

    def append(self, other):
        current = self.first
        while current.has_next():
            current = current.get_next()
        
        current.set_next(other)

    def to_print(self):
        current = self.first

        while current != None:
            print(current.get_data(), end='')
            print("-->", end='')
            current = current.get_next()

        print("None")   

        

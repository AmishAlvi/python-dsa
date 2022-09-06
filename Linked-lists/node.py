class Node:
    
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next
    
    def get_data(self):
        return self.data
    
    def set_next(self, next):
        self.next = next
    
    def set_data(self, data):
        self.data = data

    def has_next(self):
        if self.next is None:
            return False
        else:
            return True

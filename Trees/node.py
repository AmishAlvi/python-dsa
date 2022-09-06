class Node:

    def __init__(self, data = None,): 
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    def get_children(self):
        return self.children
    
    def get_child(self, childIndex):
        return self.children[childIndex]

    
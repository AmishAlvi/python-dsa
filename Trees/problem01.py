'''
create a function find_sum(root) 
such that when given the root node find_sum() 
returns the sum of all the Nodes in the Tree
'''
import node, tree 

def find_sum(root):
    children = root.getChildren()

    if children is None:
        return root.data
    else:
        pass
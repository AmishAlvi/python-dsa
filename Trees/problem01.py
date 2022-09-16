'''
create a function find_sum(root) 
such that when given the root node find_sum() 
returns the sum of all the Nodes in the Tree
'''
import node, tree 

def find_sum(root):
    children = root.get_children()
    sum = 0;
    for c in children:
        sum = sum + find_sum(c)

    return sum + root.data

node1 = node.Node(1)
node3 = node.Node(3)
node2 = node.Node(2)
node4 = node.Node(4)
node5 = node.Node(5)

node1.add_child(node2)
node1.add_child(node3)
node2.add_child(node4)
node2.add_child(node5)

tree1 = tree.Tree(node1)

print(find_sum(tree1.get_root()))
    
    
    
        
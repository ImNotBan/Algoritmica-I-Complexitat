
from preOrder import root


def main():

    # create a binary tree 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Solucio in Order: ")
    inOrderRec(root)

    print("Solucio post Order: ")
    postOrderRec(root)


def inOrderRec(root):
    if root is None:
        return
    inOrderRec(root.left)
    print(root.value)
    inOrderRec(root.right)
    
def postOrderRec(root):
    if root is None:
        return 
    postOrderRec(root.left)
    postOrderRec(root.right)
    print(root.value)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

if __name__ == "__main__":
    main()
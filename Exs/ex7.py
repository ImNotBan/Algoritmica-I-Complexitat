class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def HeightBalancedRec(array):
    if len(array) == 0:
        return None 
    
    mid = len(array) // 2
    root = Node(array[mid])
    
    root.left = HeightBalancedRec(array[:mid])
    root.right = HeightBalancedRec(array[mid+1:])
    
    return root

def inOrderRec(root):
    if root is None:
        return
    inOrderRec(root.left)
    print(root.value)
    inOrderRec(root.right)

def main():
    Array = [-10, -3, 0, 5, 9]
    root = HeightBalancedRec(Array)
    
    print("Recorregut de l'arbre in order:")
    inOrderRec(root)

if __name__ == "__main__":
    main()
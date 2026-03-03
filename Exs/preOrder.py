class root:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preOrder(root):
    if root is not None:
        print(root.value)
        preOrder(root.left)
        preOrder(root.right)

def build_tree(filename):
    nodes = {}

    with open(filename, "r") as f:
        for line in f:
            value, left, right = line.strip().split()

            if value not in nodes:
                nodes[value] = root(value)

            if left != "None":
                if left not in nodes:
                    nodes[left] = root(left)
                nodes[value].left = nodes[left]

            if right != "None":
                if right not in nodes:
                    nodes[right] = root(right)
                nodes[value].right = nodes[right]

    return nodes["1"]

if __name__ == "__main__":
    print("Solució preOrder")
    r = build_tree("arbre.txt")
    preOrder(r)

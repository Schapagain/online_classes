




# Uses Python3
import sys
import threading

def findHeight(root):
    if root == None:
        return 0
    if len(root.children) == 0:
        return 1
    child_height = max([findHeight(child) for child in root.children])
    return 1 + child_height

def main():
    class TreeNode:
        def __init__(self,val):
            self.val = val
            self.children = []

    num_nodes = int(sys.stdin.readline())
    all_nodes = list(map(int,sys.stdin.readline().split()))
    assert(len(all_nodes) == num_nodes)

    # initialize all the nodes
    tree = []
    for i in range(num_nodes):
        tree.append(TreeNode(i))

    for index,val in enumerate(all_nodes):
        if val == -1:
            root = tree[index]
        else:
            tree[val].children.append(tree[index])
    print(findHeight(root))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

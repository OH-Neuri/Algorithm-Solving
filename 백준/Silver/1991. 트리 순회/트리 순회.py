import sys

N = int(sys.stdin.readline())
tree = {}

for i in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left,right]

# 전위 순회
def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


#  중위 순회
def inorder(node):
    # 자식이 있다면
    if node !='.':
        inorder(tree[node][0])
        print(node, end = '')
        inorder(tree[node][1])

# # 후위 순회
def postorder(node):
    if node !='.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
import sys
sys.stdin = open('1991_input.txt')
# 트리 구조는 재귀(Recursion) 또는 스택/큐를 활용한 반복문(Iterative) 방식으로 접근할 수 있다.
# 이 문제에서는 이진 트리를 저장하고 순회(Traversal)하는 방법을 다룬다.


N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = (left, right)

print(tree)

# 전위 순회: 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    if node == '.':
        return
    print(node, end = '')   # 루트 출력
    preorder(tree[node][0]) # 왼쪽 자식 방문
    preorder(tree[node][1]) # 오른쪽 자식 방문

# 중위 순회: 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0]) # 왼쪽 자식 방문
    print(node, end = '') # 루트 출력
    inorder(tree[node][1]) # 오른쪽 자식 방문

# 후위 순회: 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0]) # 왼쪽 자식 방문
    postorder(tree[node][1]) # 오른쪽 자식 방문
    print(node, end = '') # 루트 출력

preorder('A')
print()
inorder('A')
print()
postorder('A')

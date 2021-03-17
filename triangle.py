# implementation of my initial approach which didn't end up working since this cannot be modeled by a binary search tree

# node class to represent elements in the triangle
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# binary tree insertion method, runs recursively
def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.data == value:
            return root
        elif root.data > value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

# traverse down the triangle, adding sum of larger element
def traverse_triangle_binary(root):
    if root.left is None and root.right is None:
        return 0
    elif root.left is not None and root.right is None:
        return root.left.data + traverse_triangle(root.left)
    elif root.right is not None and root.left is None:
        return root.right.data + traverse_triangle(root.right)
    else:
        if root.left.data >= root.right.data:
            return root.left.data + traverse_triangle(root.left)
        else:
            return root.right.data + traverse_triangle(root.right)
    return root.data



# second approach, using dynamic programming
input_text = open("triangle.txt", "r")
triangle_matrix = []
for line in input_text:
    # split up each line of triangle in its own list
    l1 = line.split(' ')
    # remove all newline elements
    if l1[len(l1)-1] == '\n':
        l1.remove(l1[len(l1)-1])
    # convert all elements to integers used for comparison later
    for num in range(len(l1)):
        l1[num] = int(l1[num])
    # append each list to triangle matrix
    triangle_matrix.append(l1)

# convert to n x n matrix, shift left and fill in 0's
for i in range(101):
    for j in range(i):
        triangle_matrix[-1*i].append(0)

# bottom up approach, compare elements below and diagonally below to the right, whichever is larger gets added to the element sum
def traverse_triangle(tri_mat): 
    for i in range(98, -1, -1): 
        for j in range(i+1): 
            if (tri_mat[i+1][j] < tri_mat[i+1][j+1]): 
                tri_mat[i][j] += tri_mat[i+1][j+1] 
            else: 
                tri_mat[i][j] += tri_mat[i+1][j]
# the maximum sum is now stored in the first element
    return tri_mat[0][0]

x = traverse_triangle(triangle_matrix)
print(x)

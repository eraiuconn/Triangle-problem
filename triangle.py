# implementation of my initial approach which didn't end up working since this cannot be modeled by a binary search tree

# node class to represent elements in the triangle
'''
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
'''

'''
-------------------------------------------
See ReadMe for updates on changes made to help this algorithm become production ready
-------------------------------------------
'''

# second approach, using dynamic programming
def setupMatrix():
    # parametrize file name
    # account for incorrect file name
    name_of_file = input("Please enter the name of the triangle text file (with extension): ")
    try:
        input_text = open(name_of_file, "r")
    except FileNotFoundError:
        print("Provided file was not found")
        return 0

    triangle_matrix = []
    missing_row_count = 0
    for line in input_text:
    # check if row is empty, program will allow up to 10 missing rows until an error is incurred
        if line == '\n':
            missing_row_count += 1
            continue
        # split up each line of triangle in its own list
        l1 = line.split(' ')
        # remove all newline elements
        if l1[len(l1)-1] == '\n':
            l1.remove(l1[len(l1)-1])
        # try to convert all elements to integers used for comparison later
        for num in range(len(l1)):
            # check if provided input is of type int, otherwise return ValueError and terminate
            # this will also fail if user inputs multiple spaces between values
            try:
                l1[num] = int(l1[num])
            except ValueError:
                print("Provided input is of the incorrect type, please input integers")
                return 0
        # append each list to triangle matrix
        triangle_matrix.append(l1)
    # check missing rows
    if missing_row_count >= 10:
            print("Too many missing rows in provided input")
            return 0
    # edge case, if only 1 line of data provided, return error
    if len(triangle_matrix) == 1:
        print("Error, triangle cannot be formed with one line of input")
        return 0
        

    # convert to n x n matrix, shift left and fill in 0's
    # conversion is now parametrized based on total input lines provided
    for i in range(len(triangle_matrix)+1):
        for j in range(i):
            triangle_matrix[-1*i].append(0)
    return triangle_matrix

# bottom up approach, compare elements below and diagonally below to the right, whichever is larger gets added to the element sum
def traverse_triangle():
    tri_mat = setupMatrix()
    # if error occurs in setting up matrix (incorrect file name, input type, missing rows, 1 row, etc.), then terminate function
    if tri_mat == 0:
        return

    # added parametrization according to size of triangle
    for i in range(len(tri_mat)-2, -1, -1): 
        for j in range(i+1): 
            if (tri_mat[i+1][j] < tri_mat[i+1][j+1]): 
                tri_mat[i][j] += tri_mat[i+1][j+1] 
            else: 
                tri_mat[i][j] += tri_mat[i+1][j]
# the maximum sum is now stored in the first element
    return tri_mat[0][0]

print(traverse_triangle())

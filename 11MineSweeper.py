# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if [row, col] in bombs:
                field[row][col]=-1;
            else:
                field[row][col]=0;
                for r in range (row-1, row+2):
                    for c in range (col-1, col+2):
                        if ([r, c] in bombs):
                            field[row][col]+=1
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]
print(to_string(mine_sweeper([[0, 2], [2, 0]], 3, 3)))
print()

# mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]
print(to_string(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)))
print()

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]
print(to_string(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)))
print()

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

# Test cases are given. The rest is my code. #

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]


def completerow(square):
    for row in square:
        for element in row:
            if element > len(square) or element%1 != 0:
                return False
            i = 0
            while i < len(square):
                if i == row.index(element):
                    i += 1
                elif row[i] == element:
                    return False
                i += 1
    return True

def transpose(square):
    transpose = []
    i = 0
    while i < len(square):
        transposerow = []
        for row in square:
            transposerow.append(row[i])
        transpose.append(transposerow)
        i += 1
    return transpose

def check_sudoku(square):
    if completerow(square) and completerow(transpose(square)):
        return True
    return False
    

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False

print check_sudoku(incorrect)
#>>> False




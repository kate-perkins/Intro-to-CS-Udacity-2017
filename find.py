def find(row, element):
    p = row
    for a in row:
        if element == a:
            return True
    return False

#print find([1,2,3],3)
#True
#print find([],3)
#False
#print find([1,2,3],4)
#False
def complete_row(row):
    for element in row:
        if element = 1:
        return True #complete


def check_sudoku(square):
    n = len(square)
    a = 0
    while a <= n and not find(square[1], square[1][a]):
        print 'hello'
        a += 1

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

print check_sudoku(correct)
print check_sudoku(incorrect)

return index number
if

list.index(1)

more than one occurence of each element in each row

a--number (1-9 for normal)
For a <= n
lkljklkj

given:
    square[a][b] <= len(square)


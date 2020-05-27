def truefor(h):
    for a in h:
        a = 0

print truefor([0,0,0])
print truefor([0,0,1])

def completerow(square):
    i = len(square)
    for row in square:
        for element in row:
            while i > 0:
                if i == square.index(element):
                    i -= 1
                if row[i] == element:
                    return False
                i -= 1
                
def find(row, element):
    for a in row:
        if element == a:
            return True
    return False
    
def check_sudoku(square):
    n = len(square)
    i = 0
    while a <= n and !find(square[1],a):
        print 'hello'

    
def completecolumn(square):
    columns = []
    for row in square:
        for element in row:
            if len(columns) < 3:
                columns.append(element)
            if len(columns) == 3:
                if len(columns[element]) 
                columns[row] = [columns[row], element]
                
def transpose(square):
    transpose = []
    n = 0
    while n < len(square) - 1:
        transposerow = []
        for row in square:
            transposerow.append(row[n])
        transpose.append(transposerow)
        n += 1
    return transpose                      

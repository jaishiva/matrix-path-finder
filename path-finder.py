all_paths=[]
temp_path =[]
class matrix():
    """docstring for ClassName"""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matr = []

        for row in range(rows):
            self.row_mat =[]
            for col in range(cols):
                self.row_mat.append(cell(row+1,col+1))
            self.matr.append(self.row_mat)



class cell():
    """docstring for cell"""
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.paths = []
        self.position = (self.row,self.col)
        


def path_finder(rows,cols):
    mat = matrix(rows,cols)
    # print(mat.matr)
    for row1 in range(rows):
        for col1 in range(cols):
            if mat.matr[row1][col1].row == rows and mat.matr[row1][col1].col == cols:
                break
            if mat.matr[row1][col1].row == rows:
                mat.matr[row1][col1].paths.append(mat.matr[row1][col1+1])
                print([row1+1,col1+1,mat.matr[row1][col1+1].position])
                continue
            if mat.matr[row1][col1].col == cols:
                mat.matr[row1][col1].paths.append(mat.matr[row1+1][col1])
                print([row1+1,col1+1,mat.matr[row1+1][col1].position])
                break
            mat.matr[row1][col1].paths.append(mat.matr[row1][col1+1])
            mat.matr[row1][col1].paths.append(mat.matr[row1+1][col1])
            # print([row1,col1,mat.matr[row1][col1+1].position,mat.matr[row1+1][col1].position])
    temp_path.append(mat.matr[0][0].position)
    find_paths(mat.matr[0][0],rows,cols)


def find_paths(cell,rows,cols):
    global all_paths
    global temp_path
    if(cell.position == (rows,cols)):
        all_paths.append(temp_path)
        temp_path = temp_path[:-1]
        return
    for path in cell.paths:
        temp_path.append(path.position)
        find_paths(path,rows,cols)
    temp_path = temp_path[:-1]

    


path_finder(4,4)
print(all_paths)


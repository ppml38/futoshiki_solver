
def futoshiki(matrix,lt,gt,size):
    def next(r,c):
        if c<(len(matrix[0])-1): return (r,c+1)
        return (r+1,0)
    def getPossibilities(row,col):
        pos=set([i for i in range(1,size+1)])
        for r in range(0,size):
            if matrix[r][col] in pos: pos.remove(matrix[r][col])
        for c in range(0,size):
            if matrix[row][c] in pos: pos.remove(matrix[row][c])
        if (row,col) in lt:
            greats=lt[(row,col)]
            for r,c in greats:
                if (n:=matrix[r][c])!=0:
                    for rm in range(n,size+1):
                        if rm in pos: pos.remove(rm)
        if (row,col) in gt:
            lesses=gt[(row,col)]
            for r,c in lesses:
                if (n:=matrix[r][c])!=0:
                    for rm in range(0,n):
                        if rm in pos: pos.remove(rm)
        return list(pos)
        
    def solve(row,col):
        if row>=len(matrix) or col>=len(matrix[0]): return True
        if matrix[row][col]==0:
            for n in getPossibilities(row,col):
                matrix[row][col]=n
                if solve(*next(row,col)): return True
            matrix[row][col]=0
        else:
            if solve(*next(row,col)): return True
        return False
    solve(0,0)
        
_matrix=[
    [0,0,0,0,0],
    [4,0,0,0,2],
    [0,0,4,0,0],
    [0,0,0,0,4],
    [0,0,0,0,0]
]
_lt={
    (0,1):[(0,0)],
    (0,3):[(0,2)],
    (0,4):[(0,3)],
    (3,3):[(3,4)],
    (4,0):[(4,1)],
    (4,1):[(4,2)]
}
_gt={
    (0,0):[(0,1)],
    (0,2):[(0,3)],
    (0,3):[(0,4)],
    (3,4):[(3,3)],
    (4,1):[(4,0)],
    (4,2):[(4,1)]
}

matrix=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,4,0,0,0]
]
lt={
    (0,4):[(0,3)],
    (1,0):[(0,0)],
    (1,1):[(1,0),(2,1)],
    (1,4):[(0,4)],
    (2,0):[(1,0),(2,1)],
    (2,1):[(2,2)],
    (3,2):[(3,3)],
    (3,3):[(3,4)],
    (4,2):[(4,3)],
    (4,3):[(3,3)],
    (4,4):[(3,4)]
}
gt={
    (0,3):[(0,4)],
    (0,0):[(1,0)],
    (0,4):[(1,4)],
    (1,0):[(1,1),(2,0)],
    (2,1):[(1,1),(2,0)],
    (2,2):[(2,1)],
    (3,3):[(3,2)],
    (3,4):[(3,3)],
    (4,3):[(4,2)],
    (3,3):[(4,3)],
    (3,4):[(4,4)]
}

futoshiki(matrix,lt,gt,5)
print(matrix)
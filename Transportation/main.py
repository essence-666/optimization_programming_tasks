def Russel():
    Z = 0
    Scopy = S.copy()
    Dcopy = D.copy()
    Ccopy =  [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for x in range(len(Scopy)):
        for y in range(len(Dcopy)):
            Ccopy[x][y] = C[x][y]
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    maxRows = []
    maxCols = []
    newC   = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    while(max(Dcopy) != 0):
        maxRows = []
        maxCols = []
        for x in range(len(Scopy)):
            maxRows.append(max(Ccopy[x]))
        for i in range(len(Dcopy)):
            maxt = 0
            for j in range(len(Scopy)):
                if(Ccopy[j][i] > maxt):
                    maxt = Ccopy[j][i]
            maxCols.append(maxt)
        for i in range(len(Scopy)):
            for j in range(len(Dcopy)):
                if(newC[i][j] != None):
                    newC[i][j] = Ccopy[i][j] - (maxRows[i] + maxCols[j])
        minValue = float("INF")
        minrow = mincolm = None
        for i in range (len(Scopy)):
            for j in range(len(Dcopy)):
             if(newC[i][j] != None):
                if(newC[i][j] < minValue):
                    minValue = newC[i][j]
                    minrow = i
                    mincolm = j
        if(Scopy[minrow]>=Dcopy[mincolm]): 
            temp = Dcopy[mincolm]
            result[minrow][mincolm] = temp
            Z = Z + C[minrow][mincolm] * temp
            Scopy[minrow] = Scopy[minrow] - temp
            Dcopy[mincolm] = Dcopy[mincolm] -temp
            for x in range(len(Scopy)):
                newC[x][mincolm] = None
                Ccopy[x][mincolm] = -1
                if(Scopy[minrow] == Dcopy[mincolm]):
                    for y in range(len(Dcopy)):
                        newC[minrow][y] = None
                        Ccopy[minrow][y] = -1
        else:
            temp = Scopy[minrow]
            result[minrow][mincolm] = temp
            Z = Z + C[minrow][mincolm] * temp
            Dcopy[mincolm] = Dcopy[mincolm] - temp
            Scopy[minrow] = Scopy[minrow] - temp
            for x in range(len(Dcopy)):
                newC[minrow][x] = None
                Ccopy[minrow][x] = -1
                if(Scopy[minrow] == Dcopy[mincolm]):
                    for y in range(len(Scopy)):
                        newC[y][mincolm] = None
                        Ccopy[y][mincolm] = -1
    print("Russle's approximtation method:")
    for row in result:
        print(' '.join(map(str, row)))


def findMax(Ccopy):
    rowdiff = []
    coldiff = []
    for i in range(len(Ccopy)):
        arr = Ccopy[i][:]
        arr.sort()
        if(arr[1] != float("INF")):
            rowdiff.append(arr[1]-arr[0])
        else:
            rowdiff.append(arr[0])
    col = 0
    while col < len(Ccopy[0]):
        arr = []
        for i in range(len(Ccopy)):
            arr.append(Ccopy[i][col])
        arr.sort()
        col+=1
        if(arr[1] != float("INF")):
            coldiff.append(arr[1]-arr[0])
        else:
            coldiff.append(arr[0])
    for x in range(len(rowdiff)):
        if(rowdiff[x] == float("INF")):
            rowdiff[x] = -1
    for x in range(len(coldiff)):
        if(coldiff[x] == float("INF")):
            coldiff[x] = -1
    if(max(rowdiff) > max(coldiff)):
        return rowdiff
    else:
        return coldiff
    

def Vogel():
    
    Scopy = S.copy()
    Dcopy = D.copy()
    Ccopy =  [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for x in range(len(Scopy)):
        for y in range(len(Dcopy)):
            Ccopy[x][y] = C[x][y]
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    Z = 0
    while(max(Dcopy) != 0 and max(Scopy) != 0):
        if(len(findMax(Ccopy)) == len(Dcopy)):
            a = findMax(Ccopy)
            tempI = 0
            tempJ = 0
            TempMin = float("INF")
            for i in range(len(Scopy)):
                for aSort in range(len(a)):
                    if(a[aSort] == float("INF")):
                        a[aSort] = -1
                temp = Ccopy[i][a.index(max(a))]
                if(temp < TempMin):
                    TempMin = temp 
                    tempI = i
                    tempJ = a.index(max(a))
            if(Scopy[tempI]>=Dcopy[tempJ]): 
                        temp = Dcopy[tempJ]
                        result[tempI][tempJ] = temp
                        Z = Z + Ccopy[tempI][tempJ] * temp
                        Scopy[tempI] = Scopy[tempI] - temp
                        Dcopy[tempJ] = Dcopy[tempJ] -temp
                        for x in range(len(Scopy)):
                            Ccopy[x][tempJ] = float("INF")
                            if(Scopy[tempI] == Dcopy[tempJ]):
                                for y in range(len(Dcopy)):
                                    Ccopy[tempI][y] = float("INF")
            else:
                temp = Scopy[tempI]
                result[tempI][tempJ] = temp
                Z = Z + Ccopy[tempI][tempJ] * temp
                Dcopy[tempJ] = Dcopy[tempJ] - temp
                Scopy[tempI] = Scopy[tempI] - temp
                for x in range(len(Dcopy)):
                    Ccopy[tempI][x] = float("INF")
                    if(Scopy[tempI] == Dcopy[tempJ]):
                        for y in range(len(Scopy)):
                            Ccopy[y][tempJ] = float("INF")
                            
        else:
            a = findMax(Ccopy)
            tempI = 0
            tempJ = 0
            TempMin = float("INF")
            for i in range(len(Dcopy)):
                for aSort in range(len(a)):
                    if(a[aSort] == float("INF")):
                        a[aSort] = -1
                temp = Ccopy[a.index(max(a))][i]
                if(temp < TempMin):
                    TempMin = temp 
                    tempI = a.index(max(a))
                    tempJ = i
            if(Scopy[tempI]>=Dcopy[tempJ]): 
                        temp = Dcopy[tempJ]
                        result[tempI][tempJ] = temp
                        Z = Z + Ccopy[tempI][tempJ] * temp
                        Scopy[tempI] = Scopy[tempI] - temp
                        Dcopy[tempJ] = Dcopy[tempJ] -temp
                        for x in range(len(Scopy)):
                            Ccopy[x][tempJ] = float("INF")
                            if(Scopy[tempI] == Dcopy[tempJ]):
                                for y in range(len(Dcopy)):
                                    Ccopy[tempI][y] = float("INF")
            else:
                temp = Scopy[tempI]
                result[tempI][tempJ] = temp
                Z = Z + Ccopy[tempI][tempJ] * temp
                Dcopy[tempJ] = Dcopy[tempJ] - temp
                Scopy[tempI] = Scopy[tempI] - temp
                for x in range(len(Dcopy)):
                    Ccopy[tempI][x] = float("INF")
                    if(Scopy[tempI] == Dcopy[tempJ]):
                        for y in range(len(Scopy)):
                            Ccopy[y][tempJ] = float("INF")
    print("Vogel's approximtation method:")
    for row in result:
        print(' '.join(map(str, row)))


def Northwest():
    Scopy = S.copy()
    Dcopy = D.copy()
    Ccopy =  [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for x in range(len(Scopy)):
        for y in range(len(Dcopy)):
            Ccopy[x][y] = C[x][y]
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    Z = 0
    while(max(Dcopy) != 0):
        for i in range(len(Scopy)):
            for j in range(len(Dcopy)):
                    if(Scopy[i]>=Dcopy[j]): 
                        temp = Dcopy[j]
                        result[i][j] = temp
                        Z = Z + Ccopy[i][j] * temp
                        Scopy[i] = Scopy[i] - temp
                        Dcopy[j] = Dcopy[j] -temp
                    else:
                        temp = Scopy[i]
                        result[i][j] = temp
                        Z = Z + Ccopy[i][j] * temp
                        Dcopy[j] = Dcopy[j] - temp
                        Scopy[i] = Scopy[i] - temp

    print("Northwest method:")
    for row in result:
        print(' '.join(map(str, row)))


def format_matrix(matrix):
    widths = [0] * len(matrix[0])
    for row in matrix:
        for i, cell in enumerate(row):
            if isinstance(cell, str):  
                widths[i] = max(widths[i], len(cell))
            elif isinstance(cell, (int, float)): 
                widths[i] = max(widths[i], len(str(int(cell))))
    formatted_rows = []
    for row in matrix:
        formatted_row = ['{:<{width}}'.format(cell, width=widths[i]) 
                         for i, cell in enumerate(row)]
        formatted_rows.append(formatted_row)
    
    return formatted_rows


S_input = input()
S = list(map(int, S_input.split()))
C = []
for _ in range(3):
    row = list(map(int, input().split()))
    C.append(row)
D_input = input()
D = list(map(int, D_input.split()))

print("Input table:")
table = [[" ","D1","D2","D3","D4","Supply"],
         ["Source 1:",0,0,0,0,0],
         ["Source 2:",0,0,0,0,0],
         ["Source 3:",0,0,0,0,0],
         ["Demands:",0,0,0,0," "]]
for x in range(len(S)):
    for y in range(len(D)):
        table[x+1][y+1] = C[x][y]
        table[x+1][y+2] =S[x]
        table[x+2][y+1] = D[y]
formatted_table = format_matrix(table)

for row in formatted_table:
    print(' | '.join(row)) 
 
Russel()
Northwest()
Vogel()
# Test #1 
# Supply vector = (50,60,25)
# Matrix of coefficients of costs =
#[3 2 7 6
# 7 5 2 3
# 2 5 4 5]
# Demand vector = (60,40,20,15)
# Input:
# 50 60 25
# 3 2 7 6
# 7 5 2 3
# 2 5 4 5
# 60 40 20 15
# Output:
# Input table:
#           | D1 | D2 | D3 | D4 | Supply
# Source 1: | 3  | 2  | 7  | 6  | 50
# Source 2: | 7  | 5  | 2  | 3  | 60
# Source 3: | 2  | 5  | 4  | 5  | 25
# Demands:  | 60 | 40 | 20 | 15 |
# Russle's approximtation method:
# 50 0 0 0
# 0 25 20 15
# 10 15 0 0
# Northwest method:
# 50 0 0 0
# 10 40 10 0
# 0 0 10 15
# Vogel's approximtation method:
# 10 40 0 0
# 25 0 20 15
# 25 0 0 0
#
#Test 2
# Supply vector = (120,280,160)
# Matrix of coefficients of costs =
#[1 7 9 5
# 4 2 6 8
# 3 8 1 2]
# Demand vector = (130,220,160,50)
#Input:
# 120 280 160
# 1 7 9 5
# 4 2 6 8
# 3 8 1 2
# 130 220 160 50
#Output:
# Input table:
#           | D1  | D2  | D3  | D4 | Supply
# Source 1: | 1   | 7   | 9   | 5  | 120
# Source 2: | 4   | 2   | 6   | 8  | 280
# Source 3: | 3   | 8   | 1   | 2  | 160
# Demands:  | 130 | 220 | 160 | 50 |
# Russle's approximtation method:
# 120 0 0 0
# 10 220 0 50
# 0 0 160 0
# Northwest method:
# 120 0 0 0
# 10 220 50 0
# 0 0 110 50
# Vogel's approximtation method:
# 120 0 0 0
# 10 220 0 50
# 0 0 160 0
#
#Test 3
# Supply vector = (22,15,8)
# Matrix of coefficients of costs =
#[6 3 5 4
# 5 9 2 7
# 5 7 8 6]
# Demand vector = (7,12,17,9)
#Input:
# 22 15 8
# 6 3 5 4
# 5 9 2 7
# 5 7 8 6
# 7 12 17 9 
#Output:
# Input table:
#           | D1 | D2 | D3 | D4 | Supply
# Source 1: | 6  | 3  | 5  | 4  | 22
# Source 2: | 5  | 9  | 2  | 7  | 15
# Source 3: | 5  | 7  | 8  | 6  | 8
# Demands:  | 7  | 12 | 17 | 9  |
# Russle's approximtation method:
# 0 12 2 8
# 0 0 15 0
# 7 0 0 1
# Northwest method:
# 7 12 3 0
# 0 0 14 1
# 0 0 0 8
# Vogel's approximtation method:
# 0 12 2 8
# 0 0 15 0
# 7 0 0 1
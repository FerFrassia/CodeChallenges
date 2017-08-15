struct Matrix {
    let rows: Int, columns: Int
    var grid: [Int]
    
    init(rows: Int, columns: Int) {
        self.rows = rows
        self.columns = columns
        self.grid = Array(repeating: 0, count: rows * columns)
    }
    
    func indexIsValid(row: Int, column: Int) -> Bool {
        return 0 <= row && row < rows && 0 <= column && column < columns
    }
    
    subscript(row: Int, column: Int) -> Int {
        get {
            assert(indexIsValid(row: row, column: column), "Index out of range")
            return grid[row * columns + column]
        }
        set {
            assert(indexIsValid(row: row, column: column), "Index out of range")
            grid[row * columns + column] = newValue
        }
    }
}

func zeroRow(m: inout Matrix, row: Int) {
    for column in 0...m.columns-1 {
        m[row, column] = 0
    }
}

func zeroColumn(m: inout Matrix, column: Int) {
    for row in 0...m.rows-1 {
        m[row, column] = 0
    }
}

func changeZero(m: Matrix) -> Matrix {
    var zeroMatrix = m
    var rowsToZero: Set<Int> = []
    var columnsToZero: Set<Int> = []
    for i in 0...m.rows-1 {
        for j in 0...m.columns-1 {
            if m[i,j] == 0 {
                rowsToZero.insert(i)
                columnsToZero.insert(j)
            }
        }
    }
    for row in rowsToZero {
        zeroRow(m: &zeroMatrix, row: row)
    }
    for column in columnsToZero {
        zeroColumn(m: &zeroMatrix, column: column)
    }
    return zeroMatrix
}


var matrix = Matrix(rows: 2, columns: 2)
matrix[0,1] = 1
matrix[0,0] = 0
matrix[1,0] = 2
matrix[1,1] = 3
assert(changeZero(m: matrix).grid == [0,0,0,3])






class Sudoku:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def check(self)-> bool:
        # проверка строк
        for i in range(len(self.matrix)):
            if check_list(self.matrix[i]) == False:
                return False
        # проверка столбцов
        for i in range(len(self.matrix[0])):
            li = [x[i] for x in self.matrix]
            if check_list(li) == False:
                return False
        # проверка квадратов
        for a in [0, 3, 6]:
            for b in [0, 3, 6]:
                li = []
                for i in range(3):
                    for j in range(3):
                        li.append(self.matrix[a+i][b+j])
                if check_list(li) == False:
                    return False
        return True
    
    def solve(self) -> bool:
        coord = find_zero_in_matr(self.matrix)
        # если вся матрица заполнена возвращаем true
        if coord == (-1,-1):
            return True
        # пробуем подставить значения и проверяем
        for i in range(1, 10, 1):
            self.matrix[coord[0]][coord[1]] = i
            if self.check():
                res = self.solve()
                if res:
                    return res
        # если ни одно значение не подходит возвращаем false   
        self.matrix[coord[0]][coord[1]] = 0    
        return False       

def find_zero_in_matr(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] == 0:
                return (i, j)
    return (-1, -1)

def print_2d_matr(matr):
    for i in range(len(matr)):
        print(matr[i])
    print('\n\r')
        
def check_list(li) -> bool:
    x = remove_in_list(li, 0)
    for num in range(1,10):
        if x.count(num) > 1:
            return False
    return True

def remove_in_list(li, elem):
    return list(filter(lambda a: a != elem, li))


if __name__ == "__main__":
    print('test1')
    matrix1 = [
        [0,0,5,0,0,0,6,0,0],
        [6,0,0,0,1,0,0,0,3],
        [0,0,4,5,0,9,1,0,0],
        [0,7,0,0,0,0,0,6,0],
        [4,6,2,0,7,0,3,5,9],
        [0,3,0,0,0,0,0,1,0],
        [0,0,6,3,0,8,2,0,0],
        [7,0,0,0,2,0,0,0,6],
        [0,0,3,0,0,0,9,0,0],
        ]
    sudoku1 = Sudoku(matrix1)
    print(sudoku1.solve())
    print_2d_matr(sudoku1.matrix)
    print('test2')
    matrix2 = [
        [5,2,0,0,1,0,0,4,3],
        [0,0,0,0,0,0,0,0,0],
        [0,3,1,0,4,0,9,8,0],
        [0,0,0,4,2,1,0,0,0],
        [0,0,4,0,0,0,6,0,0],
        [0,0,0,9,5,6,0,0,0],
        [0,7,5,0,8,0,1,3,0],
        [0,0,0,0,0,0,0,0,0],
        [8,1,0,0,3,0,0,7,2],
        ]
    sudoku2 = Sudoku(matrix2)
    print(sudoku2.solve())
    print_2d_matr(sudoku2.matrix)
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

        
def check_list(li) -> bool:
    x = remove_in_list(li, 0)
    for num in range(1,10):
        if x.count(num) > 1:
            return False
    return True

def remove_in_list(li, elem):
    return list(filter(lambda a: a != elem, li))


if __name__ == "__main__":
    matrix = [
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
    sudoku = Sudoku(matrix)
    print(sudoku.check())
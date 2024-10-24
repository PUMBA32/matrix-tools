import random


class Matrix:
    @staticmethod
    def generate(m: int = 1, n: int = 5, min: int = 0, max: int = 5) -> list[list[int]] | list[int]:
        '''генерация матрицы по заданным параметром (кол-во строк + кол-во столбцов)'''
        result: list[list[int]] = []
        if m > 0 and n > 0:
            for _ in range(m):
                result.append([random.randint(min, max) for _ in range(n)])
        return result
    

    @staticmethod
    def show(matrix: list[list[int]]) -> None:
        '''выводит матрицу в консоль в упорядоченном виде'''
        print()
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if j == 0: print("|", end=" ")
                print(f"{col}({i},{j})", end="")
                if j != len(row)-1: print(", ", end=" ")
            print(" |")
        print()


    @staticmethod
    def sum(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
        '''Сложение двух матриц с одинаковыми параметрами кол-ва строк и столбцов'''
        assert len(m1) == len(m2) and len(m1[0]) == len(m2[0]), "ошибка: параметры MxN должны совпадать у обоих матриц" 
        
        result: list[list[int]] = []
        for i, _ in enumerate(m1):
            result.append([m1[i][j] + m2[i][j] for j, _ in enumerate(m1[i])])
        return result
        
    

    @staticmethod
    def mul_on_one(m: list[list[int]], x: int) -> list[list[int]]:
        '''Умножение матрицы на число'''
        return [[col*x for col in m[i]] for i in range(len(m))]
    

    @staticmethod
    def multiply(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
        '''Умножение двух матриц'''
        assert len(m1[0]) == len(m2), "ошибка: кол-во столбцов первой матрицы должно быть равно кол-ву строк второй"

        result: list[list[int]] = []
        for i, _ in enumerate(m1):  # Проходимся по каждой строке 1й матрицы
            arr: list[int] = []
            for k, _ in enumerate(m2[0]):  # Проходимся по каждому элементу 0-ой строки 2й матрицы
                s = 0
                for j, _ in enumerate(m1[i]):  # Проходимся по каждому элементу i-ой строки 1й матрицы
                    s += m1[i][j] * m2[j][k]
                arr.append(s)    
            result.append(arr)
        return result
                
            
def main() -> None:
    m1 = Matrix.generate(3,2)
    m2 = Matrix.generate(2,3)
    Matrix.show(m1)
    Matrix.show(m2)
    Matrix.show(Matrix.multiply(m1, m2))


if __name__ == '__main__':
    main()
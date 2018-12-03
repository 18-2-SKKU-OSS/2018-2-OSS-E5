def add(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    matrix_c = []
    for i in range(rows):
        list_1 = []
        for j in range(columns):
            val = matrix_a[i][j] + matrix_b[i][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c
"""
행렬의 덧셈과 곱셈, naive한 계산방법을 이용한 구현.
덧셈함수 이용시에 두 행렬의 행의 수, 열의 수가 같아야 한다.
또한 곱셈함수 이용시 첫번째 인자배열의 열과 두번째 인자배열의 행의 차원이 서로 같아야 한다.
"""

def multiply(matrix_a, matrix_b):
    matrix_c = []
    n = len(matrix_a)
    for i in range(n):
        list_1 = []
        for j in range(n):
            val = 0
            for k in range(n):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c

"""
메인함수
"""
def main():
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    print(add(matrix_a, matrix_b))
    print(multiply(matrix_a, matrix_b))


if __name__ == '__main__':
    main()

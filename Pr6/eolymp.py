n = int(input())
matrix = []

def check(matr, n):
    for i in range(n):
        if matr[i][i] != "0":
            return "NO"
        for j in range(i + 1, n):
            if matr[i][j] != matr[j][i] or int(matr[i][j]) > 1 or int(matr[j][i]) > 1:
                return "NO"
    return "YES"


for i in range(n):
    row = input().split()
    matrix.append(row)

print(check(matrix, n))

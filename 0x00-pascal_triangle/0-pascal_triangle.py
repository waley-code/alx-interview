
def pascal_triangle(n):
    if n <= 0:
        return ([])
    y = [[1]]
    if n == 1:
        return (y)
    for i in range(n-1):
        newList = []
        newList.append(1)
        for j in range(i):
            add1 = y[i][j] + y[i][j+1]
            newList.append(add1)
        newList.append(1)
        y.append(newList)
    return (y)

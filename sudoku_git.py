def valid_solution(board):
    sumk = 0
    sumk2 = 0
    sumk3 = 0
    array = set()
    array2 = set()
    array3 = set()
    for i in board:
        for j in i:
            sumk += j
        array.add(sumk)
        sumk = 0
    # return True if 45 in array and len(array) == 1 else False
    k = 0
    for x in range(9):
        for i in board:
            for j in i[k:k + 1]:
                sumk2 += j
            array2.add(sumk2)
            sumk2 = 0
        if len(array2) == 9:
            array2.clear()
        else:
            return False
        k += 1

    k = 0
    z = 0
    for x in range(9):
        for i in board:
            for j in i[k:k + 3]:
                array3.add(j)
                z += 1
            if z == 9 and len(array3) == 9:
                z = 0
                array3.clear()

    return True if len(array2) == 0 and 45 in array and len(array) == 1 and z == 0 else False

#someting
print(valid_solution([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]))

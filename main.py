def det(lst):
    if len(lst) == 2:
        return lst[0][0] * lst[1][1] - lst[1][0] * lst[0][1]

    answer = 0
    for column in range(len(lst)):
        new_matrix = [ele[:] for ele in lst]
        new_matrix = new_matrix[1:]
        for x in range(len(new_matrix)):
            new_matrix[x].pop(column)
        answer += lst[0][column] * ((-1) ** (2 + column)) * det(new_matrix)

    return answer


if __name__ == "__main__":
    matrix = [[1, 2, 4, 5], [2, 3, 1, 1], [1, 4, 5, 8], [4, 1, 5, 3]]
    print(det(matrix))

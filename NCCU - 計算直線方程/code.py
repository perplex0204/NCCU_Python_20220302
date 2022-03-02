import numpy


def find_function(point_a, point_b):
    if point_a[0] == point_b[0]:
        answer = {
            'a': None,
            'b': None,
            'c': 0
        }
        return answer
    else:
        c = 1

    point_a = (130, 15)
    point_b = (6, 20)

    matrix1 = numpy.array([[point_a[0], 1], [point_b[0], 1]])
    matrix2 = numpy.array([point_a[1], point_b[1]])
    sol = numpy.linalg.solve(matrix1, matrix2)

    answer = {
        'a': sol[0],
        'b': sol[1],
        'c': c
    }
    return answer


print(find_function((1, 2), (1, 5)))

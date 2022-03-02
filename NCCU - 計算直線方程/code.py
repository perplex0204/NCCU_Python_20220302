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

    matrix1 = numpy.array([[point_a[0], 1], [point_b[0], 1]])
    matrix2 = numpy.array([point_a[1], point_b[1]])
    sol = numpy.linalg.solve(matrix1, matrix2)

    answer = {
        'a': sol[0],
        'b': sol[1],
        'c': c
    }
    return answer


while True:
    try:
        x1, y1 = input('請輸入第一個數組(兩個數字)，並用空白隔開：').split(' ')
        point_a = (float(x1), float(y1))
        x2, y2 = input('請輸入第二個數組(兩個數字)，並用空白隔開：').split(' ')
        point_b = (float(x2), float(y2))
        print(find_function(point_a, point_b))
    except ValueError:
        print('請重新輸入正確數值')

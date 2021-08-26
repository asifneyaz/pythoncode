# >>> pascal_triangle(3)
# [1, 3, 3, 1]
# >>> pascal_triangle(5)
# [1,5,10,10,5,1] """

def pascals_triangle(n):
    pascals_list = []
    previous = 1
    pascals_list.append(previous)
    for index in range(1, n + 1):
        current = (previous * (n-index + 1))//index
        pascals_list.append(current)
        previous = current
    print(pascals_list)


pascals_triangle(5)

arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [12, 13, 14, 15]]
result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def print_array(array):
    for i in array:
        print(f"{i}")
    print('\n')

# anti clockwise
def anti_clockwise():
    for i in range(0, 4):
        for j in range(3, -1, -1):
            result[j][i] = arr[i][3 - j]
    print_array(result)
# clockwise
def clock_wise():
    for i in range(3, -1, -1):
        for j in range(0, 4):
            result[j][i] = arr[3 - i][j]
    print_array(result)


if __name__ == '__main__':
    print('Before Rotation:')
    print_array(arr)
    print('Anti-Clockwise Rotation')
    anti_clockwise()
    print('Clockwise Rotation')
    clock_wise()

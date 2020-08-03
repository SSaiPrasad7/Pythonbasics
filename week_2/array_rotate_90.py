class Rotation:
    def __init__(self, n):
        self.arr = []
        self.result = [[] * n] * n
        self.n = n

    def input_array(self):
        for i in range(self.n):
            a = []
            for j in range(self.n):
                a.append(int(input(f'Enter the element value arr[{i}][{j}]:')))
            self.arr.insert(i, a)
        self.print_array(self.arr)

    def anti_clockwise_rotation(self):
        for i in range(0, self.n):
            for j in range((self.n - 1), -1, -1):
                self.result[j][i] = self.arr[i][(self.n - 1) - j]
        self.print_array(self.arr)

    def clockwise_rotation(self):
        for i in range((self.n - 1), -1, -1):
            for j in range(0, self.n):
                self.result[j][i] = self.arr[(self.n - 1) - i][j]
        self.print_array(self.arr)

    def print_array(self, array):
        for i in array:
            print(i)
        print('\n')


if __name__ == '__main__':
    size = int(input('Enter array size(n):'))
    rotate_90 = Rotation(size)
    rotate_90.input_array()
    rotate_90.anti_clockwise_rotation()

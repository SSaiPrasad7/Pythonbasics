#SPIRAL
class Spiral:
    def __init__(self,n):
        self.n=n
        self.arr=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        self.x, self.y = 0, 0
        self.current_value=n-1
        self.dir='RIGHT'
    def main(self):
        for i in range(1,self.n*self.n+1):
            self.arr[self.x][self.y]=i
            self.next_move(self.dir)
        self.print_array()
    def next_move(self,dir):
        if dir=='RIGHT':
            if self.y<self.current_value:
                self.y+=1
                self.dir='RIGHT'
            else:
                self.x+=1
                self.dir='DOWN'

        elif dir=='DOWN':
            if self.x < self.current_value:
                self.x += 1
                self.dir='DOWN'
            else:
                self.y-=1
                self.dir='LEFT'

        elif dir=='LEFT':
            if self.y>=(len(self.arr)-self.current_value):
                self.y-=1
                self.dir='LEFT'
            else:
                self.x-=1
                self.dir='UP'
        elif dir=='UP':
            if self.x>(len(self.arr)-self.current_value):
                self.x-=1
                self.dir='UP'
            else:
                self.current_value-=1
                self.y+=1
                self.dir='RIGHT'
    def print_array(self):
        for i in self.arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__ == '__main__':
    size=input('Enter the size of an array:')
    Spiral(int(size)).main()
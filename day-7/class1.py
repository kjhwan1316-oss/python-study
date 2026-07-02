class Board:
    def set_data(self, title, writer):
        self.title = title #self: 자바의 this와 같은 의미 
        #오른쪽: 호출할 때 받은 매개변수값, 왼쪽: 객체의 맴버변수
        self.writer = writer
        self.cnt=0

    def cntup(self):
        self.cnt +=1

# Board board1 =new Board() -> 자바
board1 = Board() #객체변수 = 클래스(매개변수)  
board2 = Board()
board1.set_data("레미제라블", "장발장")  
board2.set_data("홍길동전", "홍길동")  

board1.cntup()
board1.cntup()
board2.cntup()
print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)
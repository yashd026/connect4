# IMPORTING LIBRARIES
import random
import sys

from ui_4connect import *

class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.show()
        self.setupUi(self)
        self.initialization()
        self.pushButton.clicked.connect(self.toss)
# CONNECTING SIGNALS TO SLOTS
        self.pushButton_3.clicked.connect(lambda: self.move(0))
        self.pushButton_4.clicked.connect(lambda: self.move(1))
        self.pushButton_5.clicked.connect(lambda: self.move(2))
        self.pushButton_6.clicked.connect(lambda: self.move(3))
        self.pushButton_7.clicked.connect(lambda: self.move(4))
        self.pushButton_8.clicked.connect(lambda: self.move(5))
        self.pushButton_9.clicked.connect(lambda: self.move(6))

# INITIALIZATION
    def initialization(self):
        self.winner = None
        self.turn = "X"
        self.board = \
            [
                # 0     1     2     3     4     5     6
                [None, None, None, None, None, None, None],  # 0
                [None, None, None, None, None, None, None],  # 1
                [None, None, None, None, None, None, None],  # 2
                [None, None, None, None, None, None, None],  # 3
                [None, None, None, None, None, None, None],  # 4
                [None, None, None, None, None, None, None]   # 5
            ]
        self.boa = \
            [
                # 0        1             2         3         4         5         6
                [self.L1, self.label_8, self.L13, self.L19, self.L25, self.L31, self.L37],  # 0
                [self.L2, self.L8, self.L14, self.L20, self.L26, self.L32, self.L38],       # 1
                [self.L3, self.L9, self.L15, self.L21, self.L27, self.L33, self.L39],       # 2
                [self.L4, self.L10, self.L16, self.L22, self.L28, self.L34, self.L40],      # 3
                [self.L5, self.L11, self.L17, self.L23, self.L29, self.L35, self.L41],      # 4
                [self.L6, self.L12, self.L18, self.L24, self.L30, self.L36, self.L42]       # 5
            ]

# TOSS
    def toss(self):
        lst = [self.lineEdit.text(), self.lineEdit_2.text()]
        self.ran = str(random.choice(lst))
        self.pushButton_2.setText(self.ran)
        self.label_7.setText(self.ran + "'s" + " turn...")
        if self.ran == self.lineEdit.text():
            self.nar = self.lineEdit_2.text()
        else:
            self.nar = self.lineEdit.text()

# GAME OVER
    def game_over(self):
        dir = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        for i in range(0, 6, 1):
            for j in range(0, 7, 1):
                for d in dir:
                    coin = self.board[i][j]
                    if coin != None:
                        flag = True
                        for k in range(1, 4, 1):
                            x = i + k * d[0]
                            y = j + k * d[1]
                            if 0 <= x < 6 and 0 <= y < 7:
                                if coin != self.board[x][y]:
                                    flag = False
                                    break
                            else:
                                flag = False
                        if flag == True:
                            self.winner = self.turn
                            return True

# CHANGE TURN
    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
            self.label_7.setText(self.nar + "'s" + " turn...")
        elif self.turn == "O":
            self.turn = "X"
            self.label_7.setText(self.ran + "'s" + " turn...")

# MOVE
    def move(self, c):
        for i in range(5, -1, -1):
            if self.board[i][c] == None:
                self.board[i][c] = self.turn
                self.boa[i][c].setText(self.turn)
                break
        if self.game_over():
            self.winner = self.turn
            self.label_7.setText("")
            if self.turn == "X":
                self.label_28.setText("Congrats! " + self.ran + " U Won")
            else:
                self.label_28.setText("Congrats! " + self.nar + " U Won")
        else:
            self.change_turn()

# SHOWING WINDOW
if __name__ == "__main__":
    app = QApplication()
    win = Window()
    sys.exit(app.exec_())

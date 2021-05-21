#Sinh viên : ĐÀO VĂN THẮNG , 18133050
# Bài Tập tuần 06, có tham khảo code của thầy Đỗ Phúc Hảo
# qua link youtube : https://www.youtube.com/watch?v=Xkthjd9is4w&fbclid=IwAR0a9LzB6NBEkcGMhQV7Jz3chIexcLCbhafEJnE1EeoduI7gChZ17vTvhvo
# em đã hiểu được 98% thuật toán AStar , chỉ còn vài chỗ là PriorityQueue làm gì trong code gốc thì em chưa coi kỹ 

import copy
from queue import PriorityQueue
from random import randint
from tkinter.constants import *

class State:
    def __init__(self, data=None, par=None, g=0, h=0, op = None):
        self.data = data  # data:dữ liệu mảng 1 chiều
        self.par = par  # par: nút cha
        self.g = g  # g: trọng số đường đi từ cái đỉnh xuất phát đến đỉnh hiện tại
        self.h = h  # h: hàm dánh giá đỉnh hiện tại so với điểm đích

    def clone(self):
        sn = copy.deepcopy(self)
        return sn

    # Từ mảng 1 chiều data in ra mảng 2 chiều 3x3
    def Print(self):
        sz = 3

        for i in range(sz):
            for j in range(sz):
                print(self.data[i * sz + j], end=' ')
            print()
        print()

    def Key(self):
        # Key: cộng tất cả phần tử lại theo chuỗi từ trái sang phải, từ trên xuống dưới
        if self.data == None:
            return None
        res = ''
        for x in self.data:
            res += (str)(x)
        return res

    def __lt__(self, other):
        # lt: hàm nào nhỏ thỳ cho lên phía trên
        if other == None:
            return False
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        if other == None:
            return False
        return self.Key() == other.Key()
#kiểm tra key của 2 hàm có bằng nhau không nếu bằng thì trả về true


class Operator:
    count = []
    def __init__(self, i):
        self.i = i
        # i=0: Up
        # i=1: Down
        # i=2: Left
        # i=3: Right

    def Up(self, s):
        if self.checkStateNull(s):
            return None
        x, y = self.findPos(s)
        if (x == 2):  # nếu vị trí số 0 ở hàng 2 => None (0, 1, 2) vì không di chuyển lên được nên trả về none
            return None
        return self.swap(s, x, y, self.i) # hoán đổi phần tử dưới và trên

    def Down(self, s):
        if self.checkStateNull(s):
            return None
        x, y = self.findPos(s)
        if x == 0:  # nếu vị trí số 0 ở hàng 0 => None (0, 1, 2) vì không di chuyển xuống được nên trả về none
            return None
        return self.swap(s, x, y, self.i)  #hoán đổi phần tử trên và dưới

    def Left(self, s):
        if self.checkStateNull(s):
            return None
        x, y = self.findPos(s)
        if y == 2:  # nếu vị trí số 0 ở cột 2 => None (0, 1, 2) vì không di chuyển trái được nên trả về none
            return None
        return self.swap(s, x, y, self.i) # hoán đổi phần tủ trái với phải

    def Right(self, s):
        if self.checkStateNull(s):
            return None
        x, y = self.findPos(s)
        if y == 0:  # nếu vị trí số 0 ở cột 0 => None (0, 1, 2) vì không di chuyển phải được ta trả về none
            return None
        return self.swap(s, x, y, self.i) #hoán đổi phần tử phải và trái

    def Move(self, s):

        if self.i == 0:
            return self.Up(s)
        if self.i == 1:
            return self.Down(s)
        if self.i == 2:
            return self.Left(s)
        if self.i == 3:
            return self.Right(s)
        print(self.i)
        return None

    # Hàm kiểm tra trạng thái của s có null hay không
    def checkStateNull(self, s):
        return s.data == None

    def swap(self, s, x, y, i):
        sz = 3
        sn = s.clone()
        x_new = x
        y_new = y
        # xet up, down
        if (i == 0):
            x_new = x - 1
            y_new = y
        if i == 1:
            x_new = x - 1
            y_new = y
        # xet left, right
        if i == 2:
            x_new = x
            y_new = y + 1
        if i == 3:
            x_new = x
            y_new = y - 1
        sn.data[x * sz + y] = s.data[x_new * sz + y_new]
        sn.data[x_new * sz + y_new] = 0
        return sn

    # hàm tìm vị trí 0
    def findPos(self, s):
        sz = 3
        for i in range(sz):
            for j in range(sz):
                if s.data[i * sz + j] == 0:
                    return i, j
        return None
    # kiểm tra đối tượng có thược open hay không
    def checkInPriority(Open, tmp):
        if (tmp == None):
            return False
        return (tmp in Open.queue)

    def equal(O, G):
        if O == None:
            return False
        return O.Key() == G.Key()

    def Path(O): # in ra các bước di chuyển
        len = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        if O.par != None:
            Operator.Path(O.par)
            Operator.count.append(len[O.op.i])
        O.Print() # in ra từng bước chạy của thuật toán



    # Số vị trí khác nhau hiệu tại của S so với vị trí G
    def Hx(S, G):
        sz = 3
        res = 0
        for i in range(sz):
            for j in range(sz):
                if S.data[i * sz + j] != G.data[i * sz + j]:
                    res += 1
        return res

    def Run():
        Open = PriorityQueue()
        Closed = PriorityQueue()
        S.g = 0
        S.h = Operator.Hx(S, G)
        Open.put(S)
        while True:
            if Open.empty():
                print('found error')
                return
            O = Open.get()
            Closed.put(O)
            if Operator.equal(O, G) == True:
                print('found')
                Operator.Path(O)
                return
            # tìm tất cả trạng thái còn lại
            for i in range(4):
                op = Operator(i)
                child = op.Move(O)
                if child == None:
                    continue
                ok1 = Operator.checkInPriority(Open, child)
                ok2 = Operator.checkInPriority(Closed, child)
                if not ok1 and not ok2:
                    child.par = O
                    child.op = op
                    child.g = O.g + 1
                    child.h = Operator.Hx(child, G)
                    Open.put(child)

    def init(num):
        G = State()
        sz = 3
        G.data = []
        for i in range(sz):
            for j in range(sz):
                G.data.append((i * sz + j + 0) % 9)
        # random ra mảng goal (mảng mong muốn)
        S = G.clone()
        for i in range(num):
            op = Operator(randint(0, 3))
            tmp = op.Move(S)
            if tmp != None:
                S = tmp
        return S, G
        # random mảng bất kì , chưa random được vị trí 0 nằm giữa
import time
t1 = time.time()
S, G = Operator.init(50)
S.Print()
G.Print()
Operator.Run()
print(Operator.count)
t2 = time.time()
timee = t2 - t1
print('time : ', t2 - t1)
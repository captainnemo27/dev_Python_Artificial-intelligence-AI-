import numpy as np

def giaithua(num):
    gt= 1
    if num==0 or num ==1 :
        return gt
    else :
        for i in range(2,num +1 ):
            gt = gt *i
        return gt
num = -1
while num < 0:
    num = int(input('Nhap so duong:'))
print('Giai thùa của num ', num, 'là :', giaithua(num))
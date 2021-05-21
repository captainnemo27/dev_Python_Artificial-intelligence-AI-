# a*x^2 + b*x + c =0
from mpmath import sqrt

print('nhập phuong trình bậc 2 :')
a = float(input('nhap gia trị a :'))
b = float(input('nhap giá trị b :'))
c = float(input('nhap giá trị c :'))

if a==0 :
    if b==0:
        if c==0:
            print('Phuong trình vô số nghiệm')
        else:
            print('phương trình vô nghiệm')
    else :
        if c==0:
            print('phương trình có nghiệm là x=0')
        else :
            print('phương trình có nghiệm là x =', -c/b)
else :
    delta = b**2 - 4*a*c
    if delta < 0 : # pt vo nghiệm
        print('phương trình vô nghiệm')
    elif delta ==0 :
        print('phương trình có 1 nghiệm x=',-b/(2*a))
    else :
        print('phương trình có nghiệm X1 = ',(-b + sqrt(delta))/(2*a))
        print('phương trình có nghiệm X2 = ',(-b - sqrt(delta))/(2*a))

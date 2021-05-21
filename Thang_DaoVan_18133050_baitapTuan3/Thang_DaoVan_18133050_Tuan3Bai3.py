import matplotlib.pyplot as plt
import numpy as np

x= np.arange(-10,10,0.2)
y= 10*x**2 -20*x
plt.plot(x,y, color = 'red',linewidth =3)

x=np.arange(-8,8,0.2)
y=2*x**3 + 9*x**2 +13*x+6
plt.plot(x,y, color='blue',linewidth=3)

plt.legend(['Hàm bậc 2','Hàm bậc 3'])
plt.xlabel('Ox')
plt.ylabel('Oy')
plt.title('Đồ thị hàm số')
plt.grid()
plt.show()
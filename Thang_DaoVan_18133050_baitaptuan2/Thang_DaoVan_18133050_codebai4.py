import numpy as np
sapxeptang =bool(int(input('nhap boolean cho sapxeptang :')))
mang = np.array([3,2,4,5,6,9,12,0,3,2,1]) #mang cho san
def hamtang(mang):
    mang = sorted(mang, reverse= False)
    return mang
def hamgiam(mang):
    mang = sorted(mang, reverse= True)
    return mang
if sapxeptang == 0 :
    print('ham giam la',hamgiam(mang))
else :
    print('ham tang la',hamtang(mang))
import pandas as pd
import numpy as np
VN_data_RetailService = pd.read_csv(r'D:\IT\AI-Artificial_Interlligence\V08.02.csv')
VN_data_RetailService.info()
#VN_data_RetailService.head()
#VN_data_RetailService.describe()

#VN_data_RetailService.loc[[2,4],['2001','2002','2003']]
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(1,8,1) :

    x=np.arange(1,19,1)
    raw_content = VN_data_RetailService.iloc[i,:]
    y=raw_content[1:]
    color_s=['blue', 'pink', 'green', 'black', 'yellow', 'red', 'green', 'Magenta', 'white', 'red']
    plt.plot(x,y, color = color_s[i], linewidth =2)
    ax.set_xticks(np.arange(1,19,1))
    ax.set_xticklabels(VN_data_RetailService.columns[1:])
carrer_name=VN_data_RetailService.iloc[1:,0]
plt.legend(carrer_name[0:])
plt.ylabel('tỷ đồng')
plt.xlabel('năm')
plt.title('Tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng theo giá thực tế phân theo địa phương chia theo Tỉnh, thành phố và Năm')



plt.show()

import matplotlib.pyplot as plt

months=[1,2,3,4,5]
Sales=[1000,1500,1200,1800,1900]

plt.plot(months,Sales,color='blue',linestyle='--',linewidth='2',marker='o',label='2025 Sales')
plt.legend()
plt.xlabel('Months')
plt.ylabel('Sales')
plt.xlim(1,6)
plt.ylim(500,2000)
plt.xticks([1,2,3,4,5],['M1','M2','M3','M4','M5'])
plt.yticks([1000,1500,1200,1800,1900],['S1','S3','S2','S4','S5'])
plt.title('Sales in the Year 2025')
plt.grid(color='gray',linestyle=':',linewidth='1')
plt.show()
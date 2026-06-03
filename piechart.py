import matplotlib.pyplot as plt
regions = ['N','S','E','W']
revenue=[3000,2000,1500,1000]
plt.pie(revenue,labels=regions,autopct='%1.1f%%',colors=['gold','skyblue','lightgreen'])
plt.title('Revenue contribution by region')
plt.show()

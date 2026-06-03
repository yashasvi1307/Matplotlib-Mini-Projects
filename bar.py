import matplotlib.pyplot as plt
product=['A','B','C','D','E']
Sales=[1000,1500,800,1200]
plt.bar(product,Sales,colors='Orange',label='Sales 2025')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Product Sales Comparison')
plt.legend()
plt.show()

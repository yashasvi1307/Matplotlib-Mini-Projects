import matplotlib.pyplot as plt
scores = [45,67,89,56,78,88,92,60,74,81,77,59,66,75,82,90,85,70,73,68]
plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Marks obtained by students')
plt.show() 

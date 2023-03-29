import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv","rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
print(data)

plt.scatter(data[:,0],data[:,3],marker="o",linewidth=2*data[:,5])
print(min(data[:,0]))
print(max(data[:,0]))
print(sum(data[:,0])/len(data[:,0]))

idx = data[:,1]==6
data_6 = data[idx,:]

for i in range(2,32):
    plt.text(data[i,0], data[i,3], s=str(data[i,5]), fontsize=10)

print('Minimalna potrošnja za automobile sa 6 cilindara:', min(data_6[:,0]))
print('Maksimalna potrošnja za automobile sa 6 cilindara:', max(data_6[:,0]))
print('Srednja vrijednost potrošnje za automobile sa 6 cilindara:', sum(data_6[:,0])/len(data_6[:,0]))

plt.xlabel('Potrošnja')
plt.ylabel('Konjske snage')
plt.title('Drugi zadatak')
plt.show()



import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv("~/Dropbox/DrugConsumption/drug_consumption.text",  sep=',')
df.columns= ["ID", "Age", "Gender", "Education", "Country", "Ethnicity", "Nscore", "Escore", "Oscore", "Ascore", "Cscore", "Impulsive", "SS", "Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack", "Ecstasy", "Heroin", "Ketamine", "Legalh", "LSD", "Meth", "Mushrooms", "Nicotine", "Semer", "VSA"]


coke= df["Coke"].to_numpy()
gender= df["Gender"].to_numpy()

cokeGender= np.column_stack((coke, gender))

# People that do not take cocaine
noCoke= cokeGender[:, 0]=='CL0'
print(noCoke)
print(noCoke.shape)

# People that are male
isMale= cokeGender[:, 1]<0
print(isMale)

# People that are female
isFemale= cokeGender[:, 1]>0
print(isFemale)


frequency= ['CL6', 'CL5', 'CL4', 'CL3', 'CL2', 'CL1', 'CL0']
cokeFreq= np.zeros((len(frequency), 1884), dtype=bool)

Male_coke= np.zeros(len(frequency))
Female_coke= np.zeros(len(frequency))
for i in range(len(frequency)):
    cokeFreq[i, :] = cokeGender[:, 0]== frequency[i]
    Male_coke[i]= np.sum(cokeFreq[i, :] & isMale)
    Female_coke[i]= np.sum(cokeFreq[i, :] & isFemale)
print(Male_coke)
print(Female_coke)

# print(gender)
# print(np.sum(gender))

######### plot cocaine use by gender
fig = plt.figure()
N= 2
ind = np.arange(N)

#bar width
width = 0.1

All_coke= np.vstack((Male_coke, Female_coke))
print(All_coke)
print(All_coke.shape)

print(All_coke[:, :1])
print(np.sum(All_coke[:, :1],  axis=1))

# print(All_coke[:, :2])
# print(np.sum(All_coke[:, :2],  axis=1))

ax = fig.add_axes([0,0,1,1])
ax.bar(ind, All_coke[:, 0], bottom=0, color  = 'r')
ax.bar(ind, All_coke[:, 1], bottom=np.sum(All_coke[:, :1], axis=1), color  = 'g')
ax.bar(ind, All_coke[:, 2], bottom=np.sum(All_coke[:, :2], axis=1), color  = 'b')
ax.bar(ind, All_coke[:, 3], bottom=np.sum(All_coke[:, :3], axis=1), color  = 'r')
ax.bar(ind, All_coke[:, 4], bottom=np.sum(All_coke[:, :4], axis=1), color  = 'g')
ax.bar(ind, All_coke[:, 5], bottom=np.sum(All_coke[:, :5], axis=1), color  = 'b')
ax.bar(ind, All_coke[:, 6], bottom=np.sum(All_coke[:, :6], axis=1), color  = 'white')
plt.show()


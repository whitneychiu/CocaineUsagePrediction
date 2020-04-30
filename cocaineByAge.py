import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv("~/Dropbox/DrugConsumption/drug_consumption.text",  sep=',')
df.columns= ["ID", "Age", "Gender", "Education", "Country", "Ethnicity", "Nscore", "Escore", "Oscore", "Ascore", "Cscore", "Impulsive", "SS", "Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack", "Ecstasy", "Heroin", "Ketamine", "Legalh", "LSD", "Meth", "Mushrooms", "Nicotine", "Semer", "VSA"]

coke= df["Coke"].to_numpy()
age= df["Age"].to_numpy()

cokeAge= np.column_stack((coke, age))
print(cokeAge)


age_cat= [-0.95197, -0.07854, 0.49788, 1.09449, 1.82213, 2.59171]




frequency= ['CL6', 'CL5', 'CL4', 'CL3', 'CL2', 'CL1', 'CL0']
age_cat_coke= np.zeros((len(frequency), len(age_cat)))

for i in range(len(frequency)):
    cokeFreq= cokeAge[:, 0]==frequency[i]
    for j in range(len(age_cat)):
        age_cat_clean= np.abs(cokeAge[:, 1] - age_cat[j]) < 0.1
        age_cat_coke[i, j]= np.sum(age_cat_clean & cokeFreq)
print(age_cat_coke)

print(np.sum(age_cat_coke[:1, :], axis= 0))

# print(np.sum(age_cat_coke))

######## plot cocaine by age
fig = plt.figure()
N= len(age_cat)
ind = np.arange(N)

width = 0.1

ax = fig.add_axes([0,0,1,1])
ax.bar(ind, age_cat_coke[0, :], bottom=0, color  = 'r')
ax.bar(ind, age_cat_coke[1, :], bottom=np.sum(age_cat_coke[:1, :], axis=0), color  = 'b')
ax.bar(ind, age_cat_coke[2, :], bottom=np.sum(age_cat_coke[:2, :], axis=0), color  = 'r')
ax.bar(ind, age_cat_coke[3, :], bottom=np.sum(age_cat_coke[:3, :], axis=0), color  = 'g')
ax.bar(ind, age_cat_coke[4, :], bottom=np.sum(age_cat_coke[:4, :], axis=0), color  = 'b')
ax.bar(ind, age_cat_coke[5, :], bottom=np.sum(age_cat_coke[:5, :], axis=0), color  = 'white')
ax.bar(ind, age_cat_coke[6, :], bottom=np.sum(age_cat_coke[:5, :], axis=0), color  = 'white')
plt.show()
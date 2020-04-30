import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv("~/Dropbox/DrugConsumption/drug_consumption.text",  sep=',')


# df.head()
# df.shape
print(df.shape)
print(df.head())

# print(list(df.columns))

# Name columns
df.columns= ["ID", "Age", "Gender", "Education", "Country", "Ethnicity", "Nscore", "Escore", "Oscore", "Ascore", "Cscore", "Impulsive", "SS", "Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack", "Ecstasy", "Heroin", "Ketamine", "Legalh", "LSD", "Meth", "Mushrooms", "Nicotine", "Semer", "VSA"]

# drugUsage = df.iloc[:,13:]
# print(df.iloc[1])

# type_counts_alcohol = df['Alcohol'].value_counts()
# alcohol= type_counts_alcohol.sort_index(ascending=False).to_numpy()
# print(alcohol)


# drug= np.empty([19, 7])

# for i in range(13, 32):
#     print(i)
#     # drug[i-13,:]= df.iloc[:,i].value_counts().sort_index(ascending=False).to_numpy()
#     print(df.iloc[:,i].value_counts().sort_index(ascending=False))
#     # print(drug[i-13,:])

# plot the usage of each drug
count= np.empty([19,7])

for i in range(13, 32):
    count[i-13,0] = np.sum(df.iloc[:,i].values == 'CL6')
    count[i-13,1] = np.sum(df.iloc[:,i].values == 'CL5')
    count[i-13,2] = np.sum(df.iloc[:,i].values == 'CL4')
    count[i-13,3] = np.sum(df.iloc[:,i].values == 'CL3')
    count[i-13,4] = np.sum(df.iloc[:,i].values == 'CL2')
    count[i-13,5] = np.sum(df.iloc[:,i].values == 'CL1')
    count[i-13,6] = np.sum(df.iloc[:,i].values == 'CL0')

print(count)

count = count.astype(int)
print(count)

    # print(df.iloc[:,i].values == 'CL0')
    # print(CL0_count[;,i])
    # break
    # drug[i-13,:]= df.iloc[:,i].value_counts().sort_index(ascending=False).to_numpy()
    # print(df.iloc[:,i].value_counts().sort_index(ascending=False))
    # print(drug[i-13,:])

fig = plt.figure()
N= 19
ind = np.arange(N)

# bar width
width = 0.1

ax = fig.add_axes([0,0,1,1])
ax.bar(ind, count[:, 0], bottom=0, color  = 'r')
ax.bar(ind, count[:, 1], bottom = np.sum(count[:,:1], axis= 1), color  = 'g')
ax.bar(ind, count[:, 2], bottom = np.sum(count[:,:2], axis= 1), color  = 'b')
ax.bar(ind, count[:, 3], bottom = np.sum(count[:,:3], axis= 1), color  = 'purple')
ax.bar(ind, count[:, 4], bottom = np.sum(count[:,:4], axis= 1), color  = 'orange')
ax.bar(ind, count[:, 5], bottom = np.sum(count[:,:5], axis= 1), color  = 'pink')
ax.bar(ind, count[:, 6], bottom = np.sum(count[:,:6], axis= 1), color  = 'white')
ax.set_xlabel('Type of drug')
ax.set_ylabel('Number of people')
ax.set_title('Drug usage frequency by different drugs')
plt.show()

# print(count[:,:1])
# print(np.sum(count[:,:1], axis= 1))




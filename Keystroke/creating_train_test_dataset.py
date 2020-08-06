#Dividing dataset of each user into training set and test set and then combining training set of different users to single data file 
"""
Created on Tue May 12 16:32:47 2020

@author: Shreya Khuwal
"""


import pandas as pd
df1=pd.read_csv('final_try_Shreya.csv')
df1=df1.drop('index',axis=1)
train1=df1.sample(frac=0.8,random_state=99)
test1=df1.loc[~df1.index.isin(train1.index),:]
train1.to_csv('user1.csv',index=False)
test1.to_csv('testuser2.csv',index=False)
df2=pd.read_csv('final_try_Neha.csv')
df2=df2.drop('index',axis=1)
train2=df2.sample(frac=0.8,random_state=99)
test2=df2.loc[~df2.index.isin(train2.index),:]
train2.to_csv('user2.csv',index=False)
test2.to_csv('testuser2.csv',index=False)
df3=pd.read_csv('final_try_Divi.csv')
df3=df3.drop('index',axis=1)
train3=df3.sample(frac=0.8,random_state=99)
test3=df3.loc[~df3.index.isin(train3.index),:]
train3.to_csv('user3.csv',index=False)
test3.to_csv('testuser3.csv',index=False)
df4=pd.read_csv('final_try_Jhala.csv')
df4=df4.drop('index',axis=1)
train4=df4.sample(frac=0.8,random_state=99)
test4=df4.loc[~df4.index.isin(train4.index),:]
train4.to_csv('user4.csv',index=False)
test4.to_csv('testuser4.csv',index=False)
df5=pd.read_csv('final_try_Purva.csv')
df5=df5.drop('index',axis=1)
train5=df5.sample(frac=0.8,random_state=99)
test5=df5.loc[~df5.index.isin(train5.index),:]
train5.to_csv('user5.csv',index=False)
test5.to_csv('testuser5.csv',index=False)
df=train1.append(train2,ignore_index=True)
df=df.append(train3,ignore_index=True)
df=df.append(train4,ignore_index=True)
df=df.append(train5,ignore_index=True)
#df1=df[['lr','rl','Lr','Rl','ll','rr','l','r','L','R','Space','Enter','cpm','y']]

df1.to_csv('train_data_final.csv',index=False)
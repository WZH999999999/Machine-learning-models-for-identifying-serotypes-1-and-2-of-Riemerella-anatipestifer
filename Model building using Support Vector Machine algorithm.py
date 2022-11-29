#The model for idendnetifing serotypes 1 and 2 of Riemerella anatipestifer using Support Vector Machine algorithm
import numpy as np
import pandas as pd
import os
path=r"Path/to/the/file/for/machine/learning"
files=os.listdir(path)
data_wzhlist=[]
for file in files:
  file='\\'+file
  tmp=pd.read_csv(path+file)
  data=tmp.values
  data=list(map(list,zip(*data)))
  data=pd.DataFrame(data)
  data.columns=data.loc[0,:]
  data=data.drop([0])
  data['strain']=file[1:-4]
  if file[1:3]=='1-': 
    data['label']='1'
  else:
    data['label']='0'
  data_wzhlist.append(data)
all_data = pd.concat(data_wzhlist)
all_data.set_index('strain',inplace=True)
all_data=all_data.fillna(0)
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC 
from sklearn import metrics
from time import time
import datetime
x=all_data.drop(['label'],axis=1)
y=all_data['label']
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=170)
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
Xtrain = scaler.fit_transform(train_x)
Xtest = scaler.transform(test_x)
Kernel=['linear','poly','rbf','sigmoid']
for kernel in Kernel:
  time0=time()
  clf=SVC(kernel=kernel,gamma='auto',degree=5,cache_size=5000).fit(train_x,train_y)
  print('The accuracy under kernel %s is %f' % (kernel,clf.score(test_x,test_y)))
  print(datetime.datetime.fromtimestamp(time()-time0).strftime('%M:%S:%f')) #View the performance of the classifier under different kernel functions

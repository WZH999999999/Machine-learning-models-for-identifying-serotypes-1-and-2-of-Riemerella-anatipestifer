#The model for idendnetifing serotype 1 and 2 among Riemerella anatipestifer using Random Forest algorithm
import numpy as np
import pandas as pd
import os
path=r"Path/to/the/file/for/machine/learning"
files=os.listdir(path)
data_list=[]
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
  data_list.append(data)
all_data = pd.concat(data_list)
all_data.set_index('strain',inplace=True)
all_data=all_data.fillna(0)
#Random Forest Classifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
x=all_data.drop(['label'],axis=1)
y=all_data['label']
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=150)
rfc=RandomForestClassifier(random_state=150)
model_one=rfc.fit(train_x,train_y)
prediction=model_one.predict(test_x)
metrics.accuracy_score(prediction,test_y)

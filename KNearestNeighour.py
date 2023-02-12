#Commented on GITHUB today
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model,preprocessing
from sklearn.model_selection import train_test_split

data=pd.read_csv("car.data")

le=preprocessing.LabelEncoder()

buying=le.fit_transform(list(data["buying"]))
maint=le.fit_transform(list(data["maint"]))
door=le.fit_transform(list(data["door"]))
persons=le.fit_transform(list(data["persons"]))
lug_boot=le.fit_transform(list(data["lug_boot"]))
safety=le.fit_transform(list(data["safety"]))
cls=le.fit_transform(list(data["class"]))

X=list(zip(buying,maint,door,persons,lug_boot,safety))
y=list(cls)

x_train,x_test,y_train,y_test= train_test_split(X,y,test_size=0.1)

model=KNeighborsClassifier(n_neighbors=7)
model.fit(x_train,y_train)
acc = model.score(x_test,y_test)
print(acc)

predicted= model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

print(predicted)

for x in range(len(predicted)):
    print("predicted: ", names[predicted[x]], "data: ",x_test[x], "Actual: ",names[y_test[x]])
    n= model.kneighbors([x_test[x]],7,True)
    print("N: ",n)
    

# -*- coding: utf-8 -*-
import numpy as np
import pickle

#loading the saving model
load_model=pickle.load(open("C:\Machine Learning\RandomForest.sav","rb"))

input_data=(37,130,283,0,98,0.0,1,2,0,2)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)
result=load_model.predict(input_data_reshaped)
print(result)

if result==1:
  print("Posiblitity of having Heart Disease")
else:
  print("No Posibility of Heart Disease, your Health is good!")
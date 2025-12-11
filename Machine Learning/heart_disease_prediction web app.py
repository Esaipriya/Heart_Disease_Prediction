# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 20:40:36 2025

@author: esaip
"""

import numpy as np
import pickle
import streamlit as st

#loading the saving model
load_model=pickle.load(open("C:\Machine Learning\RandomForest.sav","rb"))


#creating a funtion for prediction

def heart_disease_prediction(input_data):
    
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)
    result=load_model.predict(input_data_reshaped)
    print(result)

    if result==1:
      return "Posiblitity of having Heart Disease"
    else:
      return "No Posibility of Heart Disease, your Health is good!"
      
  
    
def main():
    
    
    #giving a title
    st.title("Heart Disease Prediction Web App")
    
    #getting the input data from the user
    #'Age','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','Oldpeak','ST_Slope','ExerciseAngina_Y'
    Age = st.text_input("Enter a Age")
    ChestPainType = st.text_input("Enter a ChestPainType")
    RestingBP = st.text_input("Enter a RestingBP value")
    Cholesterol=st.text_input("Enter a cholestrol value")
    FastingBS = st.text_input("Enter a FastingBS Value")
    RestingECG = st.text_input("Enter a RestingECG value")
    MaxHR = st.text_input("Enter a MaxHR value")
    Oldpeak = st.text_input("Enter a Oldpeak")
    ST_Slope = st.text_input("Enter a ST-Slope")
    ExerciseAngina_Y =st.text_input("Enter a ExerciseAngina value")
    
    #code for prediction
    diagnosis =  ""
    
    #creating button for prediction
    if st.button("Heart Disease Test Result"):
        diagnosis = heart_disease_prediction([Age,ChestPainType ,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,Oldpeak,ST_Slope,ExerciseAngina_Y])
    
    
    
    st.success(diagnosis)
    
    
    
if __name__ =="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
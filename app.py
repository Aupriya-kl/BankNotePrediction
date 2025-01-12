# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 06:49:10 2025

@author: kulal
"""

import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pickle
import pandas as pd

app=FastAPI()

pickle_in=open("model.pkl","rb")
model=pickle.load(pickle_in)

@app.get('/')
def index():
    return{"BankNoteClassification"}

@app.post('/predict')
def predict_banknote(data:BankNote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction=model.predict([[variance,skewness,curtosis,entropy]])
    if (prediction[0]>0.5):
        prediction="fake note"
    else:
        prediction="its a bnk note"
    return{
           'prediction':prediction
        }
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
    
    
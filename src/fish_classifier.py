# We are importing the libraries
import uvicorn 
from fastapi import FastAPI, File, UploadFile
from prediction_script import predict_fish_class
import os
import shutil

# We are creating the app object
app = FastAPI()

@app.get('/')
# printing a welcome option
def welcome():
    return {'message':'Welcome to the Fish Classifier API'}

@app.post('/predict')
async def predict(file:UploadFile=File(...)):
    with open(file.filename,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    category = predict_fish_class(file.filename)
    return {'Type of Fish':f'{category}'}


if __name__=="__main__":
    uvicorn.run(app,host = '127.0.0.1',port=8000)
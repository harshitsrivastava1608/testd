import uvicorn
from fastapi import FastAPI,File,UploadFile
app=FastAPI()
@app.get('/')
def index():
    return{"message":"Hello,Hi Stranger"};
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome ':f'{name}'};
@app.get('/{name}')
def get_name2(name: str):
    return {'Welcome ':f'{name}'};
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
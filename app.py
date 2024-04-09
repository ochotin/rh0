from fastapi import FastAPI, Request
import numpy as np
import pandas as pd
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World2"}
	
if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)
 


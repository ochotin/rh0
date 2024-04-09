from fastapi import FastAPI, Request
import numpy as np
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
 


from http import client
from typing import Optional
from fastapi import FastAPI, Body, status
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from simplejson import JSONEncoder
from bson.objectid import ObjectId
import datetime

import models


app = FastAPI()
load_dotenv()


origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


mongoUrl = os.getenv('DATABASE_URL')

client = MongoClient(mongoUrl)
db = client['inConnDemo']


# print(test.find_one())

@app.get("/")
def read():
    return {"message": "Hello World"}

@app.post("/add-asset", response_description="Add new asset", response_model=models.Asset)
async def add_asset(asset: models.Asset = Body(...)):
    assets =  db["assets"]
    # assetAncestor = []
    # parent = asset.parent
    # if parent is not None and len(parent) > 0:
    #     ancestor = assets.find_one({"name": parent[0].name }, {"_id": 0})
    #     if ancestor.ancestor is None:
    #         assetAncestor.append(parent)
    #     else:
    #         assetAncestor = ancestor
    #         assetAncestor.append(parent)
    # asset.ancestor = assetAncestor
    
    assets.insert_one(asset.dict())
    return assets.find_one({"name": asset.name}, {"_id":0})

@app.get("/fetch-parents")
async def fetch_parents():
    assets = db["assets"]
    result = assets.find({}, {"_id": 0})
    _result = []
    for x in result:
        _result.append(x)
    return _result




# @app.put("/asset/add-parent/{asset_id}", response_model=models.Asset)
# def update_parent(asset_name: str, asset: models.Asset = Body(...)):
#     #find the asset, add data in parent 
#     assets = db["assets"]
#     asset = assets.find_one({ "name": asset_name }, )
#     #find the ancestor of parent
#     #new ancestor is [ancestor[parent], parent]


   
    


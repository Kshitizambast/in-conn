from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional

import schemas, models

router = APIRouter(
    prefix="/assets",
    tags=['Posts']
)

@router.post("/", status_code=HTTP_201_CREATED, response_model=schemas.Asset)
def addAsset(asset: schemas.Asset):
    newAsset = schemas.Asset


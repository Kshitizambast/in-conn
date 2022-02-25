from datetime import datetime
from optparse import Option
from typing import Optional
from pydantic import BaseModel
from bson import ObjectId

class Asset(BaseModel):
    _id: ObjectId
    name: str
    seller: str
    description: str
    ancestor:Optional[list] = None
    parent: Optional[str] = None
    createdOn:  Optional[str]
    updatedOn: Optional[str]




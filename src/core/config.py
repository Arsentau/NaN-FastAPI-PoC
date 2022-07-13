from pydantic import BaseModel
from typing import List

class Api(BaseModel):
    version: str
    title: str
    debug: bool

class AllowedCors(BaseModel):
    hosts: List[str]
    methods: List[str]
    headers: List[str]

class Config(BaseModel):
    api: Api
    allowed_cors: AllowedCors
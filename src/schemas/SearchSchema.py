from pydantic import BaseModel, Field, field_validator
from .enums import ResponseEnum
from datetime import datetime

class SearchDocumentRequest(BaseModel):
    query:str = Field(..., min_length=1, max_length=200)
    
    @field_validator("query")
    @classmethod
    def validate_query(cls, value):
        value = value.strip()
        
        if not value:
            raise ValueError(ResponseEnum.EmptyQuery.value)
        
        return value
    
class SearchDocumentItem(BaseModel):
    id:str
    name:str
    original_filename:str
    file_size:int
    created_at:datetime
    category:str

    
class SearchDocumentResponse(BaseModel):
    results : list[SearchDocumentItem]
    total:int
    
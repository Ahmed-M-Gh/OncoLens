from datetime import datetime, timezone
from bson import ObjectId

def build_document_record(name:str,
                          category_id:ObjectId,
                          file_id:ObjectId,
                          original_filename:str,
                          content_type:str,
                          file_size:int) -> dict:
    
    return {
        "name" : name,
        "category_id" : category_id,
        "file_id" : file_id,
        "original_filename" : original_filename,
        "content_type" : content_type,
        "file_size" : file_size,
        "created_at" : datetime.now(timezone.utc)
    }
    
from .connection import db

document_collection = db["documents"]
category_collection = db["categories"]

def create_indexes():
    
    # prevent duplicate category slug
    category_collection.create_index(
        "slug",
        unique=True
    )
    
    # speed up category filtering
    document_collection.create_index(
        "category_id"
    )
    
    # speed up category name lookup
    document_collection.create_index(
        "name"
    )
    
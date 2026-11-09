from gridfs import GridFSBucket
from .connection import db

bucket = GridFSBucket(db)

def upload_file(file_stream,
                filename:str,
                metadata:dict = None):
    
    file_id = bucket.upload_from_stream(
        filename,
        file_stream,
        metadata=metadata or {}
    )
    
    return file_id


def delete_file(file_id):
    bucket.delete(file_id)
    
def get_file(file_id):
    return bucket.open_download_stream(file_id)
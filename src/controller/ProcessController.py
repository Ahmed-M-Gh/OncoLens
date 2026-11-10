"""
Responsible for Uploading and Searching for files 
"""
from pathlib import Path
from fastapi import HTTPException, status
from src.config import get_settings
settings = get_settings()
from src.schemas.db_schemas.collections import document_collection, category_collection
from src.schemas.db_schemas.document_DB_schema import build_document_record
from src.schemas.db_schemas.gridfs_storage import upload_file, delete_file
from src.schemas.enums import ResponseEnum
import re 
from src.schemas import SearchDocumentRequest

###################
# PDF VALIDATION
###################

def validate_pdf(file):
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ResponseEnum.FilenameRequired.value
        )
        
    if Path(file.filename).suffix.lower() != ".pdf" :
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=ResponseEnum.PDFOnly.value
        )
        
    
    file.file.seek(0)
    file_signature = file.file.read(5)
    file.file.seek(0)
    
    if file_signature != b"%PDF-":
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=ResponseEnum.InvalidPDFFile.value
        )
        
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)
    
    max_size = settings.MAX_UPLOAD_SIZE_MG *1024*1024
    
    if file_size > max_size:
        raise HTTPException(
            status_code=status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE,
            detail=ResponseEnum.FileSizeLimit.value
        )
        
    return file_size


###################
# Upload Doc Logic
###################
def upload_document(request):
    file_id = None
    
    try:
        # Step 1 : validate PDF
        file_size = validate_pdf(request.file)
        
        # step 2 : Find Category
        category = category_collection.find_one(
            {"slug" : request.category.value}
        )
        
        if not category :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=ResponseEnum.NotFoundCategory.value
            )
            
        # step 3 : Upload PDF to GridFS
        file_id = upload_file(
            file_stream=request.file.file,
            filename=request.file.filename,
            metadata={
                "name" : request.name,
                "category_id" : category["_id"]
            }
        )
        
        
        # Step 4 : Build Document metaData
        document_record = build_document_record(
            name=request.name,
            category_id=category["_id"],
            file_id=file_id,
            original_filename=request.file.filename,
            content_type=request.file.content_type or "application/pdf",
            file_size=file_size
        )
        
        # step 5 : Save metadata
        document_collection.insert_one(document_record)
        
        # Step 6 : return result
        return {
            "message" : ResponseEnum.FileUploadSuccess.value
        }
    
    except HTTPException:
        raise
    
    except Exception as error:
        
        if file_id is not None:
            try:
                delete_file(file_id)
                
            except Exception: pass
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ResponseEnum.FileUploadFailed.value
        ) from error
        
    finally :
        request.file.file.close()
        
        

###################
# Search Doc Logic
###################
def search_document(request: SearchDocumentRequest):
    # Step 1 : Paper Search query
    query = re.escape(request.query.strip())
    
    # Step 2 : Build Search filter
    search_filter = {
        "name" : {
            "$regex" : query,
            "$options" : "i"
        }
    }
    
    # Step 3 : Search in mongoDB
    documents = document_collection.find(search_filter).sort("created_at", -1)
    
    # Step 4 : format results
    results = []
    
    for document in documents:
        category = category_collection.find_one({
            "_id" : document["category_id"]
        })
        
        results.append({
            "id" : str(document["_id"]),
            "name" : document["name"],
            "original_filename" : document["original_filename"],
            "file_size" : document["file_size"],
            "created_at" : document["created_at"],
            "category" : category["slug"] if category else "UNKNOWN"
        })
        
    # step 5 : return results
    return {
        "results" : results,
        "total" : len(results)
    }
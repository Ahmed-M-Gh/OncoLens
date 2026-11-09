
"""
Responsible for defining API routes
for document processing operations.
"""

from fastapi import APIRouter, Depends, status
from src.controller.ProcessController import upload_document
from src.schemas.UploaderSchema import UploadDocumentRequest, UploadDocumentResponse

process_route = APIRouter(
    prefix="/api/v0.1.0/documents",
    tags=["Documents"]
)

@process_route.post("/upload", response_model=UploadDocumentResponse,
                    status_code=status.HTTP_201_CREATED)
def upload_document_endpoint(request:UploadDocumentRequest = Depends()):
    return upload_document(request)

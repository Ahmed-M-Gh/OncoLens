
"""
Responsible for defining API routes
for document processing operations.
"""

from fastapi import APIRouter, Depends, status
from src.controller import upload_document, search_document
from src.schemas import UploadDocumentRequest, UploadDocumentResponse, SearchDocumentResponse, SearchDocumentRequest

process_route = APIRouter(
    prefix="/api/v0.1.0/documents",
    tags=["Documents"]
)

@process_route.post("/upload", response_model=UploadDocumentResponse,
                    status_code=status.HTTP_201_CREATED)
def upload_document_endpoint(request:UploadDocumentRequest = Depends()):
    return upload_document(request)


@process_route.post("/search", response_model=SearchDocumentResponse,
                    status_code=status.HTTP_200_OK)
def search_document_endpoint(request:SearchDocumentRequest):
    return search_document(request)
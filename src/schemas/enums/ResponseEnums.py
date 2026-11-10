from enum import Enum

class ResponseEnum(str, Enum):
    
    FileValidatedSuccess = "file_validate_successfully"
    FileTypeNotSupported = "file_type_not_supported"
    
    FileUploadSuccess = "file_upload_success"
    FileUploadFailed = "file_upload_failed"
    
    MognoDBNameNotFound = "mongodb_name_not_found"
    MognoDBURLNotFound = "mongodb_url_not_found"
    
    FilenameRequired = "filename_required"
    PDFOnly = "only_PDF_files_accepted"
    InvalidPDFFile = "invalid_pdf_file"
    FileSizeLimit = "file_size_exceeded_the_allowed_limit"
    
    NotFoundCategory = "category_not_found"
    
    EmptyQuery = "search_query_can't_be_empty"
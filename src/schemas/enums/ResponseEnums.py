from enum import Enum

class ResponseEnum(str, Enum):
    
    FileValidatedSuccess = "file_validate_successfully"
    FileTypeNotSupported = "file_type_not_supported"
    
    FileUploadSuccess = "file_upload_success"
    FileUploadFailed = "file_upload_failed"
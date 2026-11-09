from pydantic import BaseModel
from fastapi import UploadFile, Form, File
from enum import Enum
from .enums import ResponseEnum

class ResearchCategory(str, Enum):
    CLINICAL_STUDIES = "cancer-clinical-studies"
    CLINICAL_TRIALS = "cancer-clinical-trials"
    META_ANALYSES = "cancer-meta-analyses"
    REVIEW_PAPERS = "cancer-review-papers"
    DRUG_RESISTANCE = "drug-resistance-cancer-cases"
    MOLECULAR_BIOLOGY = "molecular-biology-cancer-mechanisms"
    TARGETED_THERAPY = "targeted-therapy-cancer-cases"

# Can't be Pydantic model because of multipart-schema
class UploadDocumentRequest:
    def __init__(self, name:str=Form(...), category:ResearchCategory=Form(...), file:UploadFile=File(...)):
        self.name = name
        self.category = category
        self.file = file
    
class UploadDocumentResponse(BaseModel):
    message:ResponseEnum
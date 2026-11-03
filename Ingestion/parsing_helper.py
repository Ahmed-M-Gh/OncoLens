"""
OncoLens - Hybrid PDF parsing Helper

====================================

purpose
-------
This module defines the architecture , shared data structures, routing rules merge helpers, and quality checks for the OncoLens PDF Processing pipeline.

Hybrid Parsing Strategy:
-------------------------
1. GROBIO:
    - Primary Source for scientific-paper metadata:
      title, author, affiliations, abstract, publication year, journal, DOI, keywords when available.
    - Extracts Scientific section hierarchy and bibliographic references.
    - GRPBIO commonly returns TEI XML. keep the original TEI output for traceability and debugging
    
2. Docling:

3. Marker:

4. Merge:

5. Quality Control:

6. Cleaning:

7. Storage:

Important Design decisions
--------------------------



"""
from enum import Enum
from dataclasses import dataclass, field
from typing import Any

# Some Schema
class PDFType(str, Enum):
    Text_BASED = "TEXT_BASED"
    SCANNED = "SCANNED"
    COMPLEX_LAYOUT = "COMPLEX_LAYOUT"
    MIXED = "MIXED"
    UNKOWN = "UNKNOWN"
    
class QualityStatus(str, Enum):
    PASSED = "passed"
    REVIEW = "review"
    FAILED = "failed"

class PaperStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PARTIAL = "partial"
    NOT_RUN = "not_run"


@dataclass
class FieldValue:
    """A value Together with it's origin and extraction status."""
    value:Any = None
    source:str|None = None
    status:str = "missing"
    confidence:float|None = None
    
@dataclass
class PageFeatures:
    """page-level signals produced by the PDF inception/Classification step."""
    page_number:int = 0
    character_count:int = 0
    text_block_count:int = 0
    image_count:int = 0
    image_coverage:float = 0.0
    column_count:int|None = None
    is_probably_scanned:bool = False
    
    
@dataclass
class PDFInception:
    """Document-level Inception result. keep page-level features."""
    file_name:str = None
    file_hash:str|None = None
    page_count:int = 0
    pdf_type:PDFType = PDFType.UNKOWN
    pages:list[PageFeatures] = field(default_factory=list)
    warning:list[str] = field(default_factory=list)
    
@dataclass
class Section:
    section_id:str
    heading:str
    text:str=""
    level:int|None = None
    page_numbers:list[int] = field(default_factory=list)
    tables:list[dict[str, Any]] = field(default_factory=list)
    figures:list[dict[str, Any]] = field(default_factory=list)
    source:str = "docling"
    matched_grobid_heading:str|None = None
    heading_match_score:float|None = None
    
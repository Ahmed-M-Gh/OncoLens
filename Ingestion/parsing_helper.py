"""
OncoLens - Hybrid PDF parsing Helper

====================================

purpose
-------
This module defines the architecture , shared data structures, routing rules merge helpers, and quality checks for the OncoLens PDF Processing pipeline.

Hybrid Parsing Strategy:
-------------------------
1. GROBIO:

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


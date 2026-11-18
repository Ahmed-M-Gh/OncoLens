"""
File To parse PDFs Texts
using Hyprid Parsing Techniques using PyMuPDF Module and Unstructured[hi-res]
"""
from pathlib import Path
import fitz

def parse_pdf_with_pymupdf(pdf_path:str|Path) -> dict:
    """
    Extract PDF MetaData, page text, and text blocks using PyMuPDF
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF Not Found : {pdf_path}")
    
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF Files are supported")
    
    result = {
        "file_name" : pdf_path.name,
        "metadata" : {},
        "total_pages" : 0,
        "pages" : []
    }
    
    with fitz.open(pdf_path) as doc:
        result["metadata"] = doc.metadata or {}
        result["total_pages"] = doc.page_count
        
        for page_index, page in enumerate(doc):
            blocks = []
            
            extracted_blocks = page.get_text(
                "blocks",
                sort=False
            )
            
            for block in extracted_blocks:
                
                # skip non Text blocks
                if len(block) < 7 or block[6] != 0:
                    continue
                
                blocks.append({
                    "text" : block[4].strip(),
                    "bbox" : {
                        "x0" : block[0],
                        "y0" : block[1],
                        "x1" : block[2],
                        "y1" : block[3],
                    }
                })
                
            page_data = {
                "page_number" : page_index+1,
                "text" : page.get_text("text", sort=False),
                "blocks" : blocks
            }
            
            result["pages"].append(page_data)
    
    return result

from unstructured.partition.pdf import partition_pdf

def parse_pdf_with_unstructured(pdf_path:str|Path):
    """
    Extract document Elements, layout, classification, figure, Captions, and tables
    using Unstructured with 'hi_res' strategy
    """
    
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
            raise FileNotFoundError(f"PDF Not Found : {pdf_path}")
        
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF Files are supported")
    
    # Using hi_res strategy to extract elements with hight quality
    elements = partition_pdf(
        filename=str(pdf_path),
        strategy="hi_res",
        infer_table_structure=True,
        chunking_strategy=None
    )        
    parsed_elements = []
    
    for element in elements:
        element_data = {
            "category" : element.category,
            "text" : element.text,
            "metadata" : {
                "page_number" : element.metadata.page_number,
                "coordinates" : element.metadata.coordinates.to_dict() if element.metadata.coordinates else None
            }
        }
        
        if element.category == "Table" and hasattr(element.metadata, "text_as_html"):
            element_data["metadata"]["text_as_html"] = element.metadata.text_as_html
        
        parsed_elements.append(element_data)
        
    return parsed_elements


def parse_pdf(pdf_path:str|Path) -> dict:
    """
    Main Orchestrator function for the hybrid pdf processing approach.
    Combines PyMuPDF (for reliable native texts & blocks) with
    Unstructured Hi_res (for element classification & captions).
    """
    
    pdf_path = Path(pdf_path)
    
    print(f"processing PDF With PyMuPDF: {pdf_path.name}...")
    pymupdf_result = parse_pdf_with_pymupdf(pdf_path)
    
    print(f"processing PDF With Unstructured (Hi_res): {pdf_path.name}...")
    unstructured_elements = parse_pdf_with_unstructured(pdf_path)
    
    # combine the results
    final_result = {
        "file_name" : pymupdf_result["file_name"],
        "metadata" : pymupdf_result["metadata"],
        "total_pages" : pymupdf_result["total_pages"],
        "pymupdf_pages" : pymupdf_result["pages"],
        "unstructured_elements" : unstructured_elements
    }
    
    return final_result
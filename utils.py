from fastapi import UploadFile, HTTPException
from config import ALLOWED_FILE_TYPES, MAX_FILE_SIZE_MB

def validate_file(file: UploadFile, content: bytes):
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400, 
            detail= f"Invalid file type, Please upload a {', '.join(ALLOWED_FILE_TYPES)} file"
            )


    size_mb = len(content) /(1024 * 1024) 
    if size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(
            status_code=400, 
            detail="File size exceeds the limit, Please upload a file less than 5MB"
            )



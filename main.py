from fastapi import FastAPI, File, UploadFile
from utils import validate_file

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "IF YOURE SEEING THIS YOU ARE AT THE RIGHT PATH"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    validate_file(file, content)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "content_type": file.content_type,
        "size_in_kb": round(len(content) / 1024, 2),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


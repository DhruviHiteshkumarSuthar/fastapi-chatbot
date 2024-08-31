from fastapi import FastAPI, UploadFile, File
from extractor import extract_text
import redis

app = FastAPI()
cache = redis.Redis(host='localhost', port=6379, db=0)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    file_content = await file.read()
    file_id = file.filename
    if cache.exists(file_id):
        return {"content": cache.get(file_id).decode('utf-8')}
    with open(file.filename, 'wb') as f:
        f.write(file_content)
    content = extract_text(file.filename)
    cache.set(file_id, content)
    return {"content": content}
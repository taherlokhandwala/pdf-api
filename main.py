from fastapi import FastAPI, HTTPException
import os
from pdfminer.high_level import extract_text

app = FastAPI()


@app.get("/get_doc_list")
def get_doc_list():
    files = os.listdir("/assets")
    return {"documents": files}


@app.get("/parse/{file_name}")
def parse(file_name: str):
    try:
        with open(f"/assets/{file_name}.pdf", "rb") as pdf:
            text = extract_text(pdf)
            return {"text": text}
    except:
        raise HTTPException(status_code=404, detail="File not found")

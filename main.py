from fastapi import FastAPI, HTTPException
import os
import pdfplumber

app = FastAPI()


@app.get("/get_doc_list")
def get_doc_list():
    files = os.listdir("/assets")
    return {"documents": files}


@app.get("/parse/{file_name}")
def parse(file_name: str):
    try:
        with pdfplumber.open(f"/assets/{file_name}.pdf") as pdf:
            text = ""
            for i in pdf.pages:
                text += i.extract_text()
            return {"text": text}
    except:
        raise HTTPException(status_code=404, detail="File not found")

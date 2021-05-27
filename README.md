## PDF parsing API

A simple API written in Python using the FastAPI module that parsers PDF files and returns its contents in a text format.

## Tools used

1. Python 3.7
2. FastAPI
3. pdfminer&nbsp;( This module parses the PDF and returns text contents. Module name : pdfminer.six )
4. Docker

## Steps to deploy server

1. `docker build -t pdf_miner .`
2. `docker run -d --name pdf_miner_container -v $PWD/assets:/assets -p 5000:5000 pdf_miner`
3. The server gets deployed at `http://localhost:5000` locally

## Endpoints

1. &nbsp;`GET : /get_doc_list`

- URL : http://localhost:5000/get_doc_list
- Output : List of document names.
- Sample response : `{ documents: ["sample_doc_1.pdf","sample_doc_2.pdf","sample_doc_3.pdf"] }`
  <br />
  <br />

2. &nbsp;`GET : /parse/{file_name}` <br /> <br />Example : `/parse/sample_doc_1`

- URL : http://localhost:5000/parse/{file_name}
- Output : Contents of `{file_name}` in text format.
- Sample response : `{ text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." }`

## Note

All PDF files must be placed inside the `assets` directory.

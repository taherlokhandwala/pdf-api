FROM python:3.7

COPY ./main.py /main.py

RUN pip install fastapi[all] pdfminer.six

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
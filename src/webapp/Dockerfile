FROM python:3.10

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src ./src

CMD ["uvicorn", "src.webapp.be.app:app", "--host", "0.0.0.0", "--port", "8000"]
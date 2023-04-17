FROM python:3.10

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY be be

COPY fe fe

CMD ["uvicorn", "be.app:app", "--host", "0.0.0.0", "--port", "8000"]
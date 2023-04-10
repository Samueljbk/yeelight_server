FROM python:3.10

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src/be/app.py .

CMD ["uvicorn", "./src/be/app.py:.", "--host", "0.0.0.0", "--port", "80"]
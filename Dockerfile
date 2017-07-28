FROM python:3.5.3-alpine

COPY flask_hello /flask_hello

WORKDIR /flask_hello

RUN pip install -r requirements.txt

EXPOSE 5555

CMD ["python","run.py"]

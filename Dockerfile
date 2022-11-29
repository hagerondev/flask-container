FROM python:3

RUN mkdir /code

WORKDIR /code

ADD . /code

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "main.py"]
FROM python:3.10

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt

EXPOSE 2020
CMD ["python3",  "/code/app.py"]

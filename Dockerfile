FROM python:3.6-alpine

RUN apk add --update build-base zlib-dev jpeg-dev freetype-dev

WORKDIR /opt/bingobot
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["BingoTest.py"]

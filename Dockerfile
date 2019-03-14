FROM alpine

MAINTAINER Simon Green "simon.green@thielsen.co.uk"

RUN apk update && \
    apk add python3 g++

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "python3 app.py" ]
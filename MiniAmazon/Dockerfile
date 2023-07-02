FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y python3-venv
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN apt-get update && \
    apt-get install -y protobuf-compiler && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install jsonfield
RUN pip install protobuf

ADD . /code/

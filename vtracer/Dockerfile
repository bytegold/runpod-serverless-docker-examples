from python:3.9-bullseye

WORKDIR /

RUN pip install runpod

ADD vtracer-linux .

ADD handler.py .

CMD [ "python", "-u", "/handler.py" ]

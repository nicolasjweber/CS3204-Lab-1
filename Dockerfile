FROM python:3.12

WORKDIR /usr/local/bin

COPY main.py .

RUN pip install numpy

CMD ["main.py"]
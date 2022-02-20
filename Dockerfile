FROM python:latest

COPY main.py message_pb2.py message.avsc requirements.txt .
RUN pip install -r requirements.txt

CMD python -u main.py

FROM python:3.10
RUN mkdir -p /opt/app 
COPY hello.py /opt/app/
CMD python /opt/app/hello.py

FROM python:3.7-slim

ADD . /code
WORKDIR /code
# RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
CMD ["python", "run.py"]

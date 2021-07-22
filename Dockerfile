FROM python:alpine3.9
COPY . /app
WORKDIR /app
RUN pip install -r flask
EXPOSE 500
CMD python ./api.py

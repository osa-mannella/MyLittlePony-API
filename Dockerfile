FROM python:alpine3.9
COPY . /app
WORKDIR /app
RUN pip install flask
EXPOSE 500
CMD python ./api.py
CMD python ./bot.py

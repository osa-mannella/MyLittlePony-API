FROM python:alpine3.9
COPY . /app
WORKDIR /app
RUN py -3 -m pip install -U discord.py
RUN pip install flask
RUN pip install aiohttp
RUN pip install python-dotenv
EXPOSE 500
CMD python ./api.py

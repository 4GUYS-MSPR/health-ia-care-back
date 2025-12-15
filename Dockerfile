FROM python

RUN apt-get update && apt-get upgrade -y
RUN mkdir /app

WORKDIR /app

COPY . /app

RUN python -m pip install -r requirements.txt
RUN chmod u+x /app/entrypoint.sh

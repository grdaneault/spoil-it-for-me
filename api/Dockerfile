FROM python:3.7-alpine

RUN adduser -D spoiler

WORKDIR /home/spoiler

COPY requirements.txt requirements.txt

RUN python -m venv venv && \
    ./venv/bin/pip install gunicorn && \
    ./venv/bin/pip install -r requirements.txt

COPY app app
COPY spoiler_api.py boot.sh ./

ENV FLASK_APP microblog.py

RUN chown -R spoiler:spoiler ./ && \
    chmod +x boot.sh

USER spoiler

EXPOSE 5000
CMD ["./boot.sh"]
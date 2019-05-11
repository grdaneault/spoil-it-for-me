FROM node:current-alpine

RUN mkdir /code
WORKDIR /code

COPY gulpfile.js package.json package-lock.json ./
RUN npm install -g gulp && \
    npm install

COPY client client

FROM node:14.18.0-alpine
WORKDIR /app
COPY /package.json /app
RUN npm install
COPY . /app
CMD npm start

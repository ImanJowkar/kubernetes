FROM node:17-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY server.js .
EXPOSE 3002

CMD ["npm", "start"]


FROM node:17-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY server.js .
EXPOSE 3001

CMD ["npm", "start"]

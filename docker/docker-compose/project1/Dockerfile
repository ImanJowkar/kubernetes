FROM nginx:alpine

WORKDIR /app

COPY nginx.conf .

RUN apk update && apk add bash

CMD ["bash"]
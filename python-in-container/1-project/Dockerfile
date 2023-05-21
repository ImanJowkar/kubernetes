FROM python:3.8.0-alpine

WORKDIR /app

RUN apk update && apk upgrade && pip install --upgrade pip

# RUN command argument1 argument2
# RUN ["command", "argument1", "argument2"]


COPY . .

# COPY --chown=root html/ /usr/share/nginx/html/
# COPY --chown=web:web html/ /usr/share/nginx/html/
# COPY --chown=1000:1000 . .

# ADD https://github.com/user/flask-app.git /app
# ADD file.tar /app


ENV name value
ENV name1=value1 name2=value2

LABEL dev=true



RUN pip install -r requirement.txt




EXPOSE 5000

# EXPOSE port/protocol
# EXPOSE 1234/udp
# EXPOSE 22/tcp

# VOLUME /app
# VOLUME ["/app"]
VOLUME /web /app


CMD ["flask", "run","--host","0.0.0.0","--port","5000"]


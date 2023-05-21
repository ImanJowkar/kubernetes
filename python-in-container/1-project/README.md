# Hello world flask app containeraization


how to use
```
docker build -t flask-app:ver1 .
docker run -it -p 5000:5000 --name flask-app flask-app:ver1

curl http://localhost:5000/hello

```


## tip
```
docker build -t flask-app:ver1 https://gitlab.com/flask-app/flask-app.git

```

## Image Layers
* **FROM**, **COPY**, **ADD** and **RUN**  add new layers to docker image.
* **WORKDIR**, **ENV**, **ENTRYPOINT**, **CMD**, **LABEL** and  etc modify Image metadata.

```
docker images --filter "label=dev=true"

```
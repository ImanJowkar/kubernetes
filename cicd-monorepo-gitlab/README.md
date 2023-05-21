Microservices project made up of 1 frontend service and 2 backend services: products & shopping-cart

#### To build the projects
    docker build -t ms-frontend:1.0 frontend
    docker build -t ms-products:1.0 products
    docker build -t ms-shopping-cart:1.0 shopping-cart

#### To start them locally (repeat for each micro service)
    cd micro-service-name 
    npm install
    npm run
    

#### To start them as docker containers - separate commands
    docker run -d -p 3000:3000 \
    -e PRODUCTS_SERVICE=host.docker.internal \
    -e SHOPPING_CART_SERVICE=host.docker.internal \
    ms-frontend:1.0

    docker run -d -p 3001:3001 ms-products:1.0
    docker run -d -p 3002:3002 ms-shopping-cart:1.0

#### To start with docker-compose (repeat for each micro service)
    export COMPOSE_PROJECT_NAME=micro-service-name (frontend)
    export DC_IMAGE_NAME=micro-service-image-name (ms-frontend)
    export DC_IMAGE_TAG=tag (1.0)
    export DC_APP_PORT=port (3000)

    docker-compose -d up


# TIP

always config containerd with insecure registry
```
    [plugins."io.containerd.grpc.v1.cri".registry]
      config_path = ""

      [plugins."io.containerd.grpc.v1.cri".registry.auths]
      [plugins."io.containerd.grpc.v1.cri".registry.configs]
        [plugins."io.containerd.grpc.v1.cri".registry.configs."gitlab.example.com:443".tls]
          insecure_skip_verify = true
        [plugins."io.containerd.grpc.v1.cri".registry.configs."gitlab.example.com:443".auth]

      [plugins."io.containerd.grpc.v1.cri".registry.headers]
      [plugins."io.containerd.grpc.v1.cri".registry.mirrors]
        [plugins."io.containerd.grpc.v1.cri".registry.mirrors."gitlab.example.com:443"]
        endpoint = ["https://gitlab.example.com:443"]

```

**add argocd user to Group as a reporter and set user and password for argocd in group space for pulling images**


**add gitlab-runner-shell to k8s-yamls repo as a owner for clone and push yaml updates.**

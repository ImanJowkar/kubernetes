# install traefic ingress controller

```

helm repo add traefik https://traefik.github.io/charts

helm install traefik traefik/traefik -f values.yaml --namespace=traefik --create-namespace


```
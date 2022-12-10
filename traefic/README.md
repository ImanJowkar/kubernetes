# install traefic ingress controller
[refrenece1](https://www.youtube.com/watch?v=dEAtD9PVr_Q&list=PL34sAs7_26wNldKrBBY_uagluNKC9cCak) \
[refrenece2](https://doc.traefik.io/traefik/getting-started/install-traefik/)

traefik is just an ingress controller, edge router and proxy

```
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm search repo traefik

helm show values traefik/traefik

helm install traefik traefik/traefik --values values.yaml -n traefik --create-namespace

k -n traefik port-forward pod/traefik-78857fcc48-znglh 9000:9000


k -n traefic get ingressroute



curl -H "From: test@example.com" nginx.example.com
```


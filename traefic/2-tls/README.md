# first you have to install pebble
[ref](https://github.com/jupyterhub/pebble-helm-chart)
```

helm install pebble pebble --repo=https://jupyterhub.github.io/helm-chart/ -n traefik -f values.yaml


```

The output is below:

```
STATUS: deployed
REVISION: 1
NOTES:
The ACME server is available at:

    https://pebble.traefik/dir
    https://localhost:32443/dir

The ACME server generates leaf certificates to ACME clients,
and signs them with an insecure root cert, available at:

    https://pebble.traefik:8444/roots/0
    https://localhost:32444/roots/0

Communication with the ACME server itself requires
accepting a root certificate in configmap/pebble:

    kubectl get configmap/pebble -o jsonpath="{.data['root-cert\.pem']}"

```
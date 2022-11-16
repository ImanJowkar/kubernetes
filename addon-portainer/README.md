# Installation Guide

```
helm repo add portainer https://portainer.github.io/k8s/
helm repo update


helm install portainer -n portainer portainer/portainer -f values.yaml


base64 tls.key | tr -d "\n"

```
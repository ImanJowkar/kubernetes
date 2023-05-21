# Kustomize

```
kubectl create deployment nginx --image nginx --dry-run=client -o yaml > deployment.yaml

wget https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv4.5.6/kustomize_v4.5.6_linux_amd64.tar.gz

tar zxf kustomize_v4.5.6_linux_amd64.tar.gz

sudo mv kustomize /usr/local/bin

kustomize build . > mydeploymet.yaml

kubectl create -k .

kubectl get all --show-labels


kustomize build overlays/prod/


kubectl create -k overlay/dev
```
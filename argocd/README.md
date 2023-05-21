# install argocd
[refrenece](https://argo-cd.readthedocs.io/en/stable/getting_started/)



```
kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo



```

## argocd-cli

```
wget argocd-binary

chmod +x argocd
mv argocd /usr/local/bin

argocd login IP_Node:Port_https

# or if you use self signed certificate use below command for login:
# argocd login IP_Node:Port_https --insecure


argocd cluster list
argocd repo list
argocd app list
argocd app get my-app

argocd proj list

argocd logout IP_Node:Port_https



argocd account get-user-info
argocd account update-password




```
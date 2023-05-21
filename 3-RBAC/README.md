# RBAC

There are two types of accounts in kubernetes: 
* User Account: is used by humans, like Admins, Developers, etc.
* Service Account: is used by machines, like Prometheus, Jenkins, etc.



```
#  create service account
kubectl create serviceaccount jenkins-sa
kubectl get sa

```
# get secret from a service account

```
# first create a service account
kubectl create serviceaccount serviceaccount_name

# then create a secret with that service account



apiVersion: v1
kind: Secret
metadata:
  name: secret-token
  annotations:
    kubernetes.io/service-account.name: serviceaccount_name
type: kubernetes.io/service-account-token


# finally you can get token 
kubectl describe secrets secret-token
```
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
# Resource Quotas

[refrence](https://kubernetes.io/docs/concepts/policy/resource-quotas/)

**If quota is enabled in a namespace for compute resources like cpu and memory, users must specify requests or limits for those values; otherwise, the quota system may reject pod creation. Hint: Use the LimitRanger admission controller to force defaults for pods that make no compute resource requirements**


```
kubectl get resourcequotas
kubectl describe quota




```
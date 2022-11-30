## Installation guide

```

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

base64 tls.key | tr -d "\n"

helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring



# or change default values.yaml and then apply with below command

helm install prom prometheus-community/kube-prometheus-stack -f values.yaml -n monitoring --create-namespace





# you can prometheus ui by port-forwarding
kubectl port-forward svc/monitoring-kube-prometheus-prometheus -n monitoring 9090:9090 &




```

## for monitor kuber-proxy change The following line in configmap
```
kubectl edit cm/kube-proxy -n kube-system

####
# kind: KubeProxyConfiguration
# metricsBindAddress: 0.0.0.0:10249
####

# and then delete the kube-proxy pod
kubectl delete pod -l k8s-app=kube-proxy -n kube-system

```

## for monitor kube-etc and kube-scheduler
```
# go to the /etc/kubernetes/manifests  and change 127.0.0.1 to 0.0.0.0

```



# good grafana dashboard

```
1860    # Node Exporter Full


```
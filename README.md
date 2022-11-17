# k8s-docs

### imperitive way to generate yaml files
```

kubectl create deployment my-deploy --image=nginx --port=80 --replicas=3 --dry-run=client -o yaml
kubectl create service clusterip test --tcp=80:80 --dry-run=client -o yaml
kubectl run my-pod --image=nginx --dry-run=client -o yaml
kubectl scale deployment nginx --replicas=6
kubectl edit deployment nginx

```



### labels and selector

```
# filter by specific label
kubectl get pod -n kube-system --show-labels
kubectl get pod -n kube-system -l k8s-app=kube-dns


# for select a pod with specific labels and update
kubectl get pod --selector="k8s-app=kube-dns" 
kubectl get deploy --selector="k8s-app=kube-dns" -n kube-system
kubectl get deploy --selector="k8s-app=kube-dns,app=nginx" -n kube-system

kubectl scale deploy --selector="k8s-app=kube-dns" --replicas=5 -n kube-system



```
 



# show pod and sort by creation

```
kubectl get po --sort-by=.metadata.creationTimestamp -n <<namespace>> | tac

kubectl get pods --sort-by=.metadata.creationTimestamp
```
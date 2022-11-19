# k8s-docs

In This [refrence](https://www.cyberithub.com/category/devops/kubernetes/page/3/) you can find good article for learning kubernetes







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



# force to delete all terminating pods
```
for p in $(kubectl get pods | grep Terminating | awk '{print $1}'); do kubectl delete pod $p --grace-period=0 --force;done

```


## difference between ReplicaSet and deployment
[refrence](https://stackoverflow.com/questions/69448131/kubernetes-whats-the-difference-between-deployment-and-replica-set)
Deployment resource makes it easier for updating your pods to a newer version.

Lets say you use ReplicaSet-A for controlling your pods, then You wish to update your pods to a newer version, now you should create Replicaset-B, scale down ReplicaSet-A and scale up ReplicaSet-B by one step repeatedly (This process is known as rolling update). Although this does the job, but it's not a good practice and it's better to let K8S do the job.

A Deployment resource does this automatically without any human interaction and increases the abstraction by one level.

Note: Deployment doesn't interact with pods directly, it just does rolling update using ReplicaSets.
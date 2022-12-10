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
kubectl patch svc you-svc -p '{"spec": {"type": "NodePort"}}'

```


## difference between ReplicaSet and deployment
[refrence](https://stackoverflow.com/questions/69448131/kubernetes-whats-the-difference-between-deployment-and-replica-set)
Deployment resource makes it easier for updating your pods to a newer version.

Lets say you use ReplicaSet-A for controlling your pods, then You wish to update your pods to a newer version, now you should create Replicaset-B, scale down ReplicaSet-A and scale up ReplicaSet-B by one step repeatedly (This process is known as rolling update). Although this does the job, but it's not a good practice and it's better to let K8S do the job.

A Deployment resource does this automatically without any human interaction and increases the abstraction by one level.

Note: Deployment doesn't interact with pods directly, it just does rolling update using ReplicaSets.


## Imperative command

```
# pod ad svc
kubectl run nginx-pod --image=nginx:alpine --dry-run=client -o yaml
kubectl run redis --image=redis:alpine --labels=tier=db --dry-run=client -o yaml
kubectl expose pod redis --name redis-service --port 6379 --target-port 6379 --dry-run=client -o yaml
kubectl explain pods --recursive | less
kubectl explain pods --recursive | grep -A10 envFrom


# deployment
kubectl create deployment webapp --image=nginx



# configmap 
kubectl create configmap config_name --from-literal=APP_COLOR=blue
kubectl create configmap app-config2 --from-literal="APP_COLOR=blue" --from-literal=APP=4


kubectl create configmap config_name --from-file=<path-to-file>

# declaritive way
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
data:
  db_data: mysql-service
  db_port: 3306



# secret

kubectl create secret generic secret_name --from-literal=DB_Host=mysql --from-literal=DB_Pass=pass


echo username | base64
echo bXl1c2Vy | base64 -d
echo -n "bXl1c2Vy" | base64 -d








```

# label in nodes 
```
kubectl label node node_name type=worker

kubectl get nodes --show-labels


```



# declare env variable which are in a file
```
export $(grep -v '^#' .env | xargs)
watch kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=node_name

```


# securityContext in Pods
[refrence](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: ubuntu
  name: ubuntu
spec:
  securityContext:
    runAsUser: 1001
    runAsGroup: 3000
    fsGroup: 2000
  containers:
  - image: ubuntu:latest
    name: ubuntu
    volumeMounts:
      - name: sec
        mountPath: /data/demo
    securityContext:
      allowPrivilegeEscalation: false
  volumes:
  - name: sec
    emptyDir: {}
  restartPolicy: Always

# ---

apiVersion: v1
kind: Pod
metadata:
  labels:
    run: ubuntu
  name: ubuntu
spec:
  containers:
  - image: ubuntu:latest
    name: ubuntu
    securityContext:
        runAsUser: 1001
        capabilities:           # capabilities are only supported at the container level not at the POD level
          add: ["MAC_ADMIN"]
  restartPolicy: Always


```

# drain, cordon, uncordon
```
kubectl drain worker-k3s --ignore-daemonsets

kubectl uncordon worker-k3s


----
kubectl cordon worker-k3s
kubectl uncordon worker-k3s

```



# tip for working with kubernetes
```
alias k="kubectl"
alias c="clear"

source <(kubectl completion bash | sed 's/kubectl/k/g')
echo "source <(kubectl completion bash)" >> ~/.bashrc


k explain <resource_name>

# switching between multiple cluster
k config use-context <context_name>


```
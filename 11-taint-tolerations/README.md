# Taint and Tolerations

**tip**: 
- taints are set on nodes
- tolerations are set on pods

kubectl taint nodes works1 key=value:taint-effect \
**tip**: there are three taint-effect: 
- **NoSchedule**   ---> pod no scheduling on the node.
- **PreferNoSchedule**  ---> the system will try to avoid placing it pod on the node but is not guaranteed.
- **NoExecute** ---> new pods will not be scheduled on the node and existing pods on the node, if any, will be evicted if they do not tolerate the taint.


```
kubectl taint nodes worker1 node=high-ram:NoSchedule

kubectl taint nodes worker1 node=high-ram:NoSchedule-  # untaint nodes

kubectl describe node node_name | grep -i taint

###########
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  tolerations:
  - key: "node"
    operator: "Equal"
    value: "high-ram"
    effect: "NoSchedule"
###########
```

# Node Selector

```
kubectl label nodes node_name size=large


#######
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  nodeSelector:
    size: large   # this is a label
#####

```




# Node Affinity
The primary prupose of node affinity feature is to ensure that pods are hosted on particular nodes.
```

apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: size
            operator: In  # In, NotIn
            values: 
            - large

```
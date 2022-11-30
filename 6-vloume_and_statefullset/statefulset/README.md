# kubernetes StatefulSets
why kubernetes have two different controllers for deploying applications: \

1. *Statefulset controller*
2. *Deployment controller*




# name convention in deployment
each pod in deployment get the name of the following pattern: \
**deployment_name**-**replicaset_hash**-**pod_hash** \

but in the statefulSet the convention of the pod name is different like below: \




# apply demo1.yaml and run a debug contaienr: 
```
kubectl apply -f demo1.yaml

kubectl run -i --tty --image busybox:1.28 dns-test --restart=Never --rm 

# in the pod run the following command

nslookup svc-normal
nslookup svc-headless

####
kubectl run -i --tty --image nginx:alpine test-pod --restart=Never --rm -- sh

curl svc-normal
curl svc-headless



####


```
# apply demo2.yaml and run a debug contaienr: 
```
kubectl apply -f demo2.yaml

kubectl run -i --tty --image busybox:1.28 dns-test --restart=Never --rm 

curl nginx-headless
nslookup nginx-headless

```

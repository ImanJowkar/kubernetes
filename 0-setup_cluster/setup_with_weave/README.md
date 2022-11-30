# Steps to Install kubernetes cluster with 3 node with containerd on Ubuntu 

[refrenece](https://computingforgeeks.com/install-kubernetes-cluster-ubuntu-jammy/)


### If you want th config firewall open the following ports 
```
6443/tcp ----> kube-apiserver
10256/tcp ---> kuber-proxy
10250/tcp ---> kubelet

2380/tcp --> etcd
2379/tcp ---> etcd






```





## Run on all Nodes


first of all you need to add hostname of all nodes in "/etc/hosts"
```
172.16.13.10 master
172.16.13.11 worker1
172.16.13.12 worker2
```

### disable swap space
netx you have to disable swap space in "/etc/fstab"
go to "/etc/fstab" and comment the following line
```
vim /etc/fstab

#/swap.img	none	swap	sw	0	0

# and then apply the following command

sudo swapoff -a
sudo mount -a
```


now your swap space must be disabled



### add required kernel modules

```
sudo modprobe overlay
sudo modprobe br_netfilter


# for persistent loading of modules

sudo tee /etc/modules-load.d/k8s.conf <<EOF
overlay
br_netfilter
EOF


```

### configure kernel parameter setting to sysctl

```
sudo tee /etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

# and run below command to apply above changes without reboot

sudo sysctl --system
```

### install containerd 
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release



sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg


echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


sudo apt-get update

sudo apt-get install containerd.io

```

#### go to containerd config file and enable Systemd_cgroup = true

```
mkdir -p /etc/containerd
containerd config default>/etc/containerd/config.toml

# changes the following line in thie containerd config.toml in /etc/containerd/config.toml

SystemdCgroup = true

systemctl restart containerd

```


### Install kubectl, kubeadm, kubelet

```
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl


sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg


echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list



sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl


```


## Run only on master node
```
# below commad will pull all required image for setup the cluster

kubeadm config images pull

```

### Initialize the cluster 

```
kubeadm init

# if everything is Ok then the following result will be returned

[init] Using Kubernetes version: v1.25.4
[preflight] Running pre-flight checks
	[WARNING SystemVerification]: missing optional cgroups: blkio
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "ca" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local master] and IPs [10.96.0.1 172.16.13.10]
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "front-proxy-ca" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "etcd/ca" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [localhost master] and IPs [172.16.13.10 127.0.0.1 ::1]
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [localhost master] and IPs [172.16.13.10 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Starting the kubelet
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[apiclient] All control plane components are healthy after 20.502212 seconds
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config" in namespace kube-system with the configuration for the kubelets in the cluster
[upload-certs] Skipping phase. Please see --upload-certs
[mark-control-plane] Marking the node master as control-plane by adding the labels: [node-role.kubernetes.io/control-plane node.kubernetes.io/exclude-from-external-load-balancers]
[mark-control-plane] Marking the node master as control-plane by adding the taints [node-role.kubernetes.io/control-plane:NoSchedule]
[bootstrap-token] Using token: 0xjehn.06edjhzg5d1j6j2i
[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
[bootstrap-token] Configured RBAC rules to allow Node Bootstrap tokens to get nodes
[bootstrap-token] Configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] Configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] Configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstrap-token] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
[kubelet-finalize] Updating "/etc/kubernetes/kubelet.conf" to point to a rotatable kubelet client certificate and key
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 172.16.13.10:6443 --token 0xjehn.06edjhzg5d1j6j2i \
	--discovery-token-ca-cert-hash sha256:62c6693c7f502b109862ddaea4856b4c7512e1e3b11aa778fec0b8a4161d2773 


```


## run The following command

```
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

```


### apply Weave CNI 
[refrenece](https://www.weave.works/docs/net/latest/kubernetes/kube-addon/)
```
# remember Pod Network IP Address Range should not overlap with Node IP Addressess

wget https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml

# change the --ipalloc-range for pod IP

vim weave.yaml
# the add the following line 





    spec:
      # Wait 5 seconds to let pod connect before rolling next pod
      selector:
        matchLabels:
          name: weave-net
      minReadySeconds: 5
      template:
        metadata:
          labels:
            name: weave-net
        spec:
          initContainers:
            - name: weave-init
              image: 'weaveworks/weave-kube:latest'
              imagePullPolicy: Always
              command:
                - /home/weave/init.sh
                - --ipalloc-range=100.32.0.0/12    ### ONLY ADD THIS LINE 
              env:
              securityContext:
                privileged: true
              volumeMounts:
                - name: cni-bin
                  mountPath: /host/opt
                - name: cni-bin2
                  mountPath: /host/home
                - name: cni-conf
                  mountPath: /host/etc
                - name: lib-modules
                  mountPath: /lib/modules
                - name: xtables-lock
                  mountPath: /run/xtables.lock
                  readOnly: false
          containers:
            - name: weave




kubectl apply -f weave.yaml

# after one year all pod are in the running state and you can join the worker node to the cluster


kubectl get pod -n kube-system

NAME                             READY   STATUS    RESTARTS      AGE
coredns-565d847f94-j4fcc         1/1     Running   0             34m
coredns-565d847f94-s2km6         1/1     Running   0             34m
etcd-master                      1/1     Running   0             34m
kube-apiserver-master            1/1     Running   0             34m
kube-controller-manager-master   1/1     Running   0             34m
kube-proxy-rx7l5                 1/1     Running   0             34m
kube-scheduler-master            1/1     Running   0             34m
weave-net-55brc                  2/2     Running   1 (66s ago)   4m48s




```

### Join the worker node to the cluster

```
# for join any worker node to the cluster run the following command


kubeadm join 172.16.13.10:6443 --token 0xjehn.06edjhzg5d1j6j2i --discovery-token-ca-cert-hash sha256:62c6693c7f502b109862ddaea4856b4c7512e1e3b11aa778fec0b8a4161d2773 

# if you lose the commad, don't worry about it you can create a new token with the following command

kubeadm token create --print-join-command

```

### Cluster is setup successfully

```

kubectl get pod -n kube-system 

NAME                             READY   STATUS    RESTARTS      AGE
coredns-565d847f94-j4fcc         1/1     Running   0             54m
coredns-565d847f94-s2km6         1/1     Running   0             54m
etcd-master                      1/1     Running   0             54m
kube-apiserver-master            1/1     Running   0             54m
kube-controller-manager-master   1/1     Running   0             54m
kube-proxy-hllhn                 1/1     Running   0             16m
kube-proxy-kb2mn                 1/1     Running   0             16m
kube-proxy-rx7l5                 1/1     Running   0             54m
kube-scheduler-master            1/1     Running   0             54m
weave-net-49zv9                  2/2     Running   0             12m
weave-net-55brc                  2/2     Running   1 (21m ago)   24m
weave-net-kq9tx                  2/2     Running   0             12m


kubectl get nodes


NAME      STATUS   ROLES           AGE   VERSION
master    Ready    control-plane   55m   v1.25.4
worker1   Ready    <none>          17m   v1.25.4
worker2   Ready    <none>          16m   v1.25.4
```


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

# and then restart the containerd

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
kubeadm init  --apiserver-advertise-address 172.16.13.10 --pod-network-cidr 10.244.0.0/16

root@master:~# kubeadm init  --apiserver-advertise-address 172.16.13.10 --pod-network-cidr 10.244.0.0/16
W1116 05:42:39.830104    1237 version.go:104] could not fetch a Kubernetes version from the internet: unable to get URL "https://dl.k8s.io/release/stable-1.txt": Get "https://storage.googleapis.com/kubernetes-release/release/stable-1.txt": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
W1116 05:42:39.830296    1237 version.go:105] falling back to the local client version: v1.25.4
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
[kubelet-check] Initial timeout of 40s passed.
[apiclient] All control plane components are healthy after 42.508033 seconds
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config" in namespace kube-system with the configuration for the kubelets in the cluster
[upload-certs] Skipping phase. Please see --upload-certs
[mark-control-plane] Marking the node master as control-plane by adding the labels: [node-role.kubernetes.io/control-plane node.kubernetes.io/exclude-from-external-load-balancers]
[mark-control-plane] Marking the node master as control-plane by adding the taints [node-role.kubernetes.io/control-plane:NoSchedule]
[bootstrap-token] Using token: 6qmw7s.ct9hvdkbkha4pey1
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

kubeadm join 172.16.13.10:6443 --token 6qmw7s.ct9hvdkbkha4pey1 \
	--discovery-token-ca-cert-hash sha256:b8754c0505b5cf1d0e7a62e45110ccb96cf235d63b4538f113f2a4dce4abe7b0 


```


## run The following command

```
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

```


### apply flannel CNI 
[refrenece](https://github.com/flannel-io/flannel)
```
# remember Pod Network IP Address Range should not overlap with Node IP Addressess

kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml

```

### Join the worker node to the cluster

```
# for join any worker node to the cluster run the following command


kubeadm join 172.16.13.10:6443 --token uq6avr.koz1b4ncdp88j4oh --discovery-token-ca-cert-hash sha256:92e6317bab5f6a5e0ee4b498c8859367d3373eddfa305b3ff26f649b9df99783 

```


# after one year :))),  all pod are in the running state and you can join the worker node to the cluster
```

kubectl get pod -n kube-flannel

NAME                        READY   STATUS    RESTARTS   AGE
pod/kube-flannel-ds-97jwx   1/1     Running   0          6m34s
pod/kube-flannel-ds-bk752   1/1     Running   0          14m
pod/kube-flannel-ds-d5vnr   1/1     Running   0          7m14s


```
```
# if you lose the commad, don't worry about it you can create a new token with the following command

kubeadm token create --print-join-command



### Cluster is setup successfully



kubectl get pod -n kube-system 

pod/coredns-565d847f94-ljhwj         1/1     Running   0             19m
pod/coredns-565d847f94-xp77h         1/1     Running   0             19m
pod/etcd-master                      1/1     Running   0             19m
pod/kube-apiserver-master            1/1     Running   0             19m
pod/kube-controller-manager-master   1/1     Running   1 (15m ago)   19m
pod/kube-proxy-4pfj6                 1/1     Running   0             8m36s
pod/kube-proxy-wlm62                 1/1     Running   0             19m
pod/kube-proxy-xbjqp                 1/1     Running   0             9m16s
pod/kube-scheduler-master            1/1     Running   1 (15m ago)   19m



kubectl get nodes


NAME      STATUS   ROLES           AGE     VERSION
master    Ready    control-plane   20m     v1.25.4
worker1   Ready    <none>          9m32s   v1.25.4
worker2   Ready    <none>          8m52s   v1.25.4
```


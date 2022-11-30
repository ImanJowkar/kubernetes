# setup k3s
```
# on master nodes
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--node-ip=172.16.93.237 --flannel-iface=ens33 --write-kubeconfig-mode=644" sh -

systemctl status k3s.service
journalctl -f --unit k3s

ls -l /var/lib/rancher/
ll /etc/rancher/
vim /var/lib/rancher/k3s/server/token # ---> token for join node to cluster

vim /etc/rancher/k3s/k3s.yaml   # ---> kube-config file for k3s


# on worker nodes
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--node-ip=172.16.93.237 --flannel-iface=ens33" K3S_URL="https://172.16.93.237:6443" K3S_TOKEN="K10214463b8947a60e9ac3434fb946a6a947867c626e9d67228152d1001f98e362d::server:65f9435be518a91e27e174e4174df46f" sh -





# run on master for test cluster
kubectl run nginx --image=nginx
kubectl expose  pod nginx --port 80 --type NodePort




# for uninstall k3s run: 

# on master: 
/usr/local/bin/k3s-uninstall.sh
rm -rf /var/lib/rancher
rm -rf /etc/rancher


# on worker:
/usr/local/bin/k3s-agent-uninstall.sh
rm -rf /var/lib/rancher
rm -rf /etc/rancher
```

## you can install k3s with mysql, postgresql and sqlite. 
[refrenece](https://www.youtube.com/watch?v=UycNiBrOX1s&list=PL34sAs7_26wPnQeGnFNfeYB1uV54AaTRX&index=3)

## you can install k3d.
[refrenece](https://www.youtube.com/watch?v=CxylDAwQQSI&list=PL34sAs7_26wPnQeGnFNfeYB1uV54AaTRX&index=4)
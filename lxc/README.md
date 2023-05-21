# linux lxd/lxc
[refrenece](https://linuxcontainers.org/lxd/getting-started-cli/)


```
dpkg -l | grep lxc
sudo snap install lxd --channel=5.0/stable
systemctl status lxc
getent group lxd
sudo gpasswd -a $USER lxd
newgrp lxd
groups


sudo lxd init
no, 
yes, 
default, 
dir
no
yes
lxdbr0


#### 
config: {}
networks:
- config:
    ipv4.address: auto
    ipv6.address: auto
  description: ""
  name: lxdbr0
  type: ""
  project: default
storage_pools:
- config: {}
  description: ""
  name: default
  driver: dir
profiles:
- config: {}
  description: ""
  devices:
    eth0:
      name: eth0
      network: lxdbr0
      type: nic
    root:
      path: /
      pool: default
      type: disk
  name: default
projects: []
cluster: null
####


lxc version
lxc help
lxc help storage
lxc storage list
lxc remote list
lxc image list
lxc image list images:
lxc image list images:cent
uname -r # all machine use the host kernel not owned kernel


lxc launch ubuntu:16.04
lxc list


lxc delete <name>
lxc stop <name>
lxc start <name>


lxc delete <name> --force
lxc launch ubuntu:22.04 u-test
lxc copy u-test u-test1
lxc start u-test1


# rename a container
lxc stop u-test
lxc move u-test my-vm
lxc list
lxc start my-vm


# login to vm
lxc exec my-vm bash


# you can ping with dns name
ping u-test1


# get info
lxc info my-vm
lxc config show my-vm
lxc profile list
lxc profile show default


lxc profile copy default custom


lxc profile edit custom



lxc launch ubuntu:16.04 myvm2 --profile custom
# add below config like this
config:   
  limits.memory: 1GB


lxc launch ubuntu:16.04 my-vm2 --profile custom



# limit resources


lxc config set my-vm limits.memory 512MB
lxc config set my-vm limits.memory 1GB
lxc config set my-vm limits.cpu 1


# how to show the number of cpu avalable on vm
nproc




# copy file to lxc containers
lxc file push ~/kubernetes/lxd_container/README.md my-vm/root/ # push
lxc file pull my-vm/root/README.md .



# snapshop
# :))) for i in $(seq 5); do mkdir $i; done


lxc snapshot my-vm snap-my-vm
lxc list #  attention to snapshot collumn
lxc restore my-vm snap-my-vm


```


# lxc profile
```








```
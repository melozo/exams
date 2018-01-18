# My notes on taking Red Hat EX436 - High Availability Clustering exam

## Objectives
Candidates should be able to perform the tasks listed below:

* Configure a high-availability cluster, using either physical or virtual systems, that:
* Utilizes shared storage.
* Provides service fail-over between the cluster nodes.
* Provides preferred node for a given service.
* Selectively fails over services based on specific constraints.
* Preemptively removes non-functioning cluster members to prevent corruption of shared storage.
* Manage logical volumes in a clustered environment:
* Create volume groups that are available to all members of a highly available cluster.
* Create logical volumes that can be simultaneously mounted by all members of a high-availability cluster.
* Configure a GFS file system to meet specified size, layout, and performance objectives.
* Configure iSCSI initiators.
* Use multipathed devices.
* Configure cluster logging.
* Configure cluster monitoring.
* As with all Red Hat performance-based exams, configurations must persist after reboot without intervention.

## Lab setup

I'm using following setup for preparation:
* ha-kvm.example.com - Server with KVM and Vagrant installed
** hosta.example.com - VM created by Vagrant, cluster member
** hostb.example.com - VM created by Vagrant, cluster member
** hostc.example.com - VM created by Vagrant, cluster member

Two networks used between KVM server and each of the VMs. Two networks is necessary for multipathing.

Install `fence-virtd` and `fence-virt` packages on ha-kvm.
We will be using multicasting for fencing, so to set up server:
* Amend `/etc/fence_virt.conf` so that fence daemon listens to the proper virbr interface.
* Open port 1229/tcp so that multicast is working between the server and nodes
* Check that fence daemon can list VMs:
    
    [root@ha-kvm ha]# fence_xvm -o list
    ha_hosta                         3b7cb5dd-6933-4a0b-89c1-26e882f50319 on
    ha_hostb                         1e5443c1-6c74-4abe-9352-c3f3623e9ba2 on
    ha_hostc                         5462eb4f-6cc5-4c45-bf39-78c79d5fb0bc on
* Generate key for fencing:

    dd if=/dev/random of=/etc/cluster/fence_xvm.key bs=4094 count=1



## Vagrant
Vagrant file for this exam is provided.
Copy it into proper folder, execute
    
    vagrant up

And in a couple of seconds all three cluster nodes should be up and running:

[root@ha-kvm ha]# vagrant status
Current machine states:

    hosta                     running (libvirt)
    hostb                     running (libvirt)
    hostc                     running (libvirt)

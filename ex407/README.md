# My notes on taking Red Hat EX407 - Red Hat Certified Specialist in Ansible Automation exam

## Objectives
Candidates should have the following skills and abilities:

* Understand core components of Ansible
* Inventories
* Modules
* Variables
* Facts
* Plays
* Playbooks
* Configuration files
* Run ad-hoc Ansible commands
* Use both static and dynamic inventories to define groups of hosts
* Utilize an existing dynamic inventory script
* Create Ansible plays and playbooks
* Know how to work with commonly used Ansible modules
* Use variables to retrieve the results of running a commands
* Use conditionals to control play execution
* Configure error handling
* Create playbooks to configure systems to a specified state
* Selectively run specific tasks in playbooks using tags
* Create and use templates to create customized configuration files
* Work with Ansible variables and facts
* Create and work with roles
* Download roles from an Ansible Galaxy and use them
* Manage parallelism
* Use Ansible Vault in playbooks to protect sensitive data
* Install Ansible Tower and use it to manage systems
* Use provided documentation to look up specific information about Ansible modules and commands
As with all Red Hat performance-based exams, configurations must persist after restart without intervention.

## Lab setup

I'm using following setup for preparation:
* ha-kvm.example.com - Server with KVM and Vagrant installed
* hosta.example.com - VM created by Vagrant, cluster member
* hostb.example.com - VM created by Vagrant, cluster member
* hostc.example.com - VM created by Vagrant, cluster member

Two networks used between KVM server and each of the VMs. Two networks are used in some tasks.

Install `ansible` package on ha-kvm.
T.B.D.

## Vagrant
Vagrant file for this exam is provided.
Copy it into proper folder, execute

```
    vagrant up
```

And in a couple of seconds all three cluster nodes should be up and running:

```
[root@ha-kvm ha]# vagrant status
Current machine states:

    hosta                     running (libvirt)
    hostb                     running (libvirt)
    hostc                     running (libvirt)
```

## Found issues

T.B.D.

```
## Useful links
[Ansible overview](https://www.redhat.com/en/technologies/management/ansible)  
[Ansible Galaxy](https://galaxy.ansible.com/)
T.B.D.

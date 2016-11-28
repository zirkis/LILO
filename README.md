# LILO
LILO is a connected greenhouse allowing you to grow your own seasonings at home.

![alt tag](https://github.com/zirkis/LILO/blob/master/images/README/lilo.png)

## Required

- [Vagrant](https://www.vagrantup.com)
	
	Plugins: vagrant-vbguest

- [Ansible](http://docs.ansible.com/ansible)

## Install
	
```bash
$ vagrant up --provision
```

## Connect

```bash
$ vagrant ssh
```

## Create database

```bash
$ TENSORFLOW #(to activate the virtualenv)

$ cd app/scripts

$ python makeDatabaseImage.py

```
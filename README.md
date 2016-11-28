# LILO
LILO is a connected greenhouse allowing you to grow your own seasonings at home.

![alt tag](https://github.com/zirkis/LILO/blob/master/images/README/lilo.png)

## Required

- [Vagrant](https://www.vagrantup.com)
	
	Plugins: vagrant-vbguest

- [Ansible](http://docs.ansible.com/ansible)

See [Help install](https://github.com/zirkis/LILO/blob/kevin/docs/installation.rst)

## Install
	
```bash
$ vagrant up --provision
```


Can take up to an hour and a half (depends on your connection and your computer)

## Connect

```bash
$ vagrant ssh
```

## Create database

```bash
$ WORKSPACE #(to activate the virtualenv)

$ cd app/scripts

$ python makeDatabaseImage.py

```
# LILO
LILO is a connected greenhouse allowing you to grow your own seasonings at home.

![alt tag](https://github.com/zirkis/LILO/blob/kevin/docs/images/lilo.png)

## Required

- [Vagrant](https://www.vagrantup.com)
	
	Plugins: vagrant-vbguest

- [Ansible](http://docs.ansible.com/ansible)

See [Help install](https://github.com/zirkis/LILO/blob/kevin/docs/installation.md)

## Install
	
```bash
$ vagrant up --provision
```

Can take up to an hour and a half (depends on your connection and your computer)

## Connect

```bash
$ vagrant ssh
```

## Create or import dataset 

[Create](https://github.com/zirkis/LILO/blob/kevin/docs/makedataset.md)

[Import](https://github.com/zirkis/LILO/blob/kevin/docs/importdataset.md)

## Retrain 

[Retrain](https://github.com/zirkis/LILO/blob/kevin/docs/retrain.md)

## Test

[Test](https://github.com/zirkis/LILO/blob/kevin/docs/test.md)
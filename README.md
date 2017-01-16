# LILO
LILO is a connected greenhouse allowing you to grow your own seasonings at home.


The goal of this project is to make the greenhouse able to recognize the species growing within it, and analyse them in order to send useful information to the user via a mobile application.

Coded in Python, with OpenCV & TensorFlow, this project follows machine learning & deep learning concepts to able computer vision.

Software by Benjamin HAOUI & Kevin DIDELOT.
Hardware provided by the french startup Prêt à Pousser (https://pretapousser.fr)

[![alt text](https://github.com/zirkis/LILO/blob/master/docs/images/lilo.png)](https://pretapousser.fr)

## Required

- [Vagrant](https://www.vagrantup.com)
	
	Plugins: vagrant-vbguest

- [Ansible](http://docs.ansible.com/ansible)

See [Help install](https://github.com/zirkis/LILO/blob/master/docs/installation.md)

## Install
	
```bash
cd <path_to_project>/vagrant
vagrant up --provision
```

Can take up to an hour and a half (depends on your connection and your computer)

## Connect

```bash
vagrant ssh
```

## Create or import dataset 

[Create](https://github.com/zirkis/LILO/blob/kevin/docs/makedataset.md)

[Import](https://github.com/zirkis/LILO/blob/kevin/docs/importdataset.md)

## Retrain 

[Retrain](https://github.com/zirkis/LILO/blob/kevin/docs/retrain.md)

## Test

[Test](https://github.com/zirkis/LILO/blob/kevin/docs/test.md)

//TODO
sudo apt-get install tesseract-ocr
pytesseract
yapf

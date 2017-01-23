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

## Collect data

First thing we have to activate the workspace env.

```bash
WORKSPACE
```

Now we have to create a folder to store all the data that we want to add in 
the future in the dataset.

```bash
mkdir data_on_preparation
```

Now we have to collect as much data as possible, they are multiple way to do it.

<p align="center">
  <img src="https://github.com/zirkis/LILO/blob/master/docs/images/prepare_data.jpeg"
  alt="multiple way to collect data"/>
</p>

### Manually

If you already have some data just create a subdirectory in `data_on_preparation` for
each label and copy paste all your data in it.

Note: Check for each subdirectories that all the data correspond to the good label

The expected result:

	data_on_preparation/
		|
		|__ plane/
		|	|__ plane_1.jpg
		|	|__ plane_2.jpg
		|	....
		|	|__ plane_n.jpg
		|__car/
		|	|__ car_1.jpg
		|	|__ car_2.jpg
		|	....
		|	|__ car_n.jpg
		|_house/
			|__ house_1.jpg
			|__ house_2.jpg
			....
			|__ house_n.jpg

The name of the images doesn't matter

Formats accepted:
- jpg
- png
- bmp

### From video

You can extract the frame from the video in order to get more data.

Just create a new script:

```bash
touch extract_frame_from_video.py
```

Then copy paste the following code, then change the path to your video, the label and 
the frequency to extract the frame (frequency=2 => One image in two will be taken) 

```python
# -*- coding: utf-8 -*-
from deep_learning import extract_frame_from_video

if __name__ == '__main__':
  
  path_to_save = 'data_on_prepare'
  path_to_video = "path/to/your/video"
  frequency = 2
  label = 'your_label'

  extract_frame_from_video(path_to_videos,
    	frequency, '{}/{}'.format(path_to_save, label))
    
```

Note: Take a frequency too low is not a good idea because the difference between the 
previous image will be very low, this will cause an over-training of your label.

Then execute the script:


```bash
python extract_frame_from_video.py
```

### From web

## Retrain 

[Retrain options](https://github.com/zirkis/LILO/blob/master/docs/retrain.md)

## Label an image

## More examples

[Examples](https://github.com/zirkis/LILO/blob/master/app/deep_learning/examples)


//TODO
sudo apt-get install tesseract-ocr
pytesseract
yapf

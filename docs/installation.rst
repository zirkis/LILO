Install opencv
==============

On linux
----------

- Install these packages:

	[compiler] sudo apt-get install build-essential

	[required] sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

	[optional] sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

- Download the archive of opencv(3.1.0)

	https://github.com/Itseez/opencv/archive/3.1.0.zip

- Extract it

	unzip 3.1.0.zip -d .

- Build opencv

	- Go in the opencv folder

		cd opencv

	- Create a folder to make the build file

		mkdir build

	- Go in the build folder

		cd build

	- Configure cmake

		cmake -D CMAKE_BUILD_TYPE=RELEASE

					-D CMAKE_INSTALL_PREFIX=/usr/local
					
					-D ENABLE_PRECOMPILED_HEADERS=OFF..

	- Make

		make -j4

- Install

	sudo make install

Install the python requirement (with pip)
=========================================

sudo pip install -r requirements.txt
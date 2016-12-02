# Make data set

Open a terminal then:

## Activate the virtualenv

```bash
WORKSPACE
```

## Go to `app/scripts` and open `makeDatabaseImage.py`

```bash
cd ~/app/scripts

(vi/emacs/subl) makeDatabaseImage.py
```

## Create an array of search

```python
searchs = ["plane", "car", "house"]
```

## Set the number of pictures to get

```python
numberOfPictures = 1000
```

## Expected result

```python
if __name__ == '__main__':

	pathToSave = "../data"

	pictureManager = PicturesManager(pathToSave)

	searchs = ["plane", "car", "house"]
	numberOfPictures = 1000

	pictureManager.downloadPictures(searchs, numberOfPictures)		
	pictureManager.convertPicturesToFormat()
```

## Launch `makeDatabaseImage.py` with python

```bash
python makeDatabaseImage.py
```

Your dataset is ready

## Note

You can go to the data's folder to check if all the images are really what you 
expect to be. If not you should delete them because it will decrease the 
efficiency of the learning.

[![alt text](https://github.com/zirkis/LILO/blob/kevin/docs/images/left-arrow.png)](https://github.com/zirkis/LILO/blob/kevin/README.MD)


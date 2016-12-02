# Make data set

Open a terminal then:

## Activate the virtualenv

```bash
WORKSPACE
```

## Go to `app/scripts` and open `makeDatabaseImage.py`

```bash
cd ~/app/scripts/training

(vi/emacs/subl) makeDatabaseImage.py
```

## Create an array of searchies

```python
searchies = ["plane", "car", "house"]
```

## Set the number of pictures to get

```python
numberOfPictures = 1000
```

## Expected result

```python
if __name__ == '__main__':

	pathToSave = "../../data"

	pictureManager = PicturesManager(pathToSave)

	searchies = ["plane", "car", "house"]
	numberOfPictures = 1000

	for search in searchies:
		pictureManager.downloadPictures(search, numberOfPictures)

	pictureManager.convertPicturesToFormat()
```

## Launch `makeDatabaseImage.py` with python

```bash
python makeDatabaseImage.py
```

Your dataset is ready

## Note

You can go to the data's folder (`~/app/data`) to check if all the images are really what you 
expect to be. If not you should delete them because it will decrease the 
efficiency of the learning.

More images you got more the learning will be efficient.

[![alt text](https://github.com/zirkis/LILO/blob/kevin/docs/images/left.png)](https://github.com/zirkis/LILO/blob/kevin/README.md)


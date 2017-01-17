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

## Create a dict of searchies

- key: folder to save

- value: search

```python
searchies = {"plane": "plane", "car": "car", "house": "house"}
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

	searchies = {"plane": "plane", "car": "car", "house": "house"}
	numberOfPictures = 10

	for folderToSave, search in searchies.iteritems():
		pictureManager.downloadPictures(search, numberOfPictures, "../../data/{}".format(folderToSave))

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

[![alt text](https://github.com/zirkis/LILO/blob/master/docs/images/left.png)](https://github.com/zirkis/LILO/blob/master/README.md)

from deep_learning.utils.dataset.pictures_manager import PicturesManager

def test_getInfosPicture():
	pictureManager = PicturesManager('pathToSave')
	result = {'dirname': 'folder',
						'name': 'image',
						'format': 'jpg'
						}
	assert pictureManager.getInfosPicture('folder/image.jpg') == result
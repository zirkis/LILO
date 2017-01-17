# Convert incorrect files

Open a terminal then:

## Activate the virtualenv

```bash
WORKSPACE
```

## Launch `make_database_image.py` with python

```bash
cd ~/app/scripts/training

python convert_incorrect_files.py
```

Your dataset is ready

## Note

This scripts will convert all your images to `jpg`. 

Accepted format :
- bmp, BMP
- jpeg, JPEG
- png, PNG
- jpg, JPG

If your images are not of in the list above they will be deleted

[![alt text](https://github.com/zirkis/LILO/blob/master/docs/images/left.png)](https://github.com/zirkis/LILO/blob/master/docs/importdataset.md)
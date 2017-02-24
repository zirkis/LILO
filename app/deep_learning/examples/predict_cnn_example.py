# -*- coding: utf-8 -*-

import argparse
from keras.models import load_model

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-w", "--weights", required=True,
	type=str, help="Path to weights file")
args = vars(ap.parse_args())

model = load_model(args["weights"])


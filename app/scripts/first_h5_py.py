# -*- coding: utf-8 -*-

import h5py
import numpy as np

f = h5py.File("data.h5", "w")

dataset = f.create_dataset("lilo_data", (100,32,32,3), dtype='i')
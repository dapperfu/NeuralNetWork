#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import h5py
from PIL import Image
import numpy as np
import os
import glob

image_list = list()
classification_list = list()

taxonomies = glob.glob("Images/*")
for i in range(len(taxonomies)):
    taxonomy = taxonomies[i]
    
    classification = np.zeros(len(taxonomies))
    classification[i]=1.0
        
    for image in glob.glob(os.path.join(taxonomy,"*.jpg")):
        image_ = Image.open(image)
        image_.resize((32,32))
        image_array = np.asarray(image_)/255
        assert(image_array.shape == (32, 32, 3))        
        classification_list.append(classification)
        
assert(len(image_list)==len(classification_list))

hdf_dataset = "imported_dataset.hdf5"
opts=dict()
opts["compression"]="gzip"
opts["compression_opts"]=9
with h5py.File(hdf_dataset, "w") as fid:
    fid.create_dataset("images", data=image_list, **opts)
    fid.create_dataset("classifications", data=classification_list, **opts)
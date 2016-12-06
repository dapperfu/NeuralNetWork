#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Naval Fate.

Usage:
  nn_import_images.py [-o FILE] <folder>
  nn_import_images.py (-h | --help)
  nn_import_images.py --version

Options:
  -h --help        Show this screen.
  --version        Show version. 
  -o FILE, --out=FILE Output hdf5 file
                      [default: imported_data.hdf5]

"""
from docopt import docopt

import glob
import h5py
import numpy as np
from PIL import Image
import os

def import_data(arguments):
    image_list = list()
    classification_list = list()
    
    folder      = arguments["<folder>"]
    hdf_dataset = arguments["--out"]
    print("Scanning "+folder)
    taxonomies = glob.glob(folder+"/*")
    for i in range(len(taxonomies)):
        taxonomy = taxonomies[i]
        print("\t"+taxonomy)
        
        classification = np.zeros(len(taxonomies))
        classification[i]=1.0
            
        for image in glob.glob(os.path.join(taxonomy,"*.jpg")):
            image_ = Image.open(image)
            image_list.append(np.asarray(image_)/255)
            classification_list.append(classification)
            
    # Check that we imported everything equally.
    assert len(image_list)==len(classification_list)
    
    image_list = np.asarray(image_list)
    classification_list = np.asarray(classification_list)
    
    opts=dict()
    opts["compression"]="gzip"
    opts["compression_opts"]=9
    print("Saving data ...", end="", flush=True)
    with h5py.File(hdf_dataset, "w") as fid:
        fid.create_dataset("images", data=image_list, **opts)
        fid.create_dataset("classifications", data=classification_list, **opts)
    print("... Done")

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    import_data(arguments)
#!/usr/bin/env python
# This script can be used to see how bitmaps will be preprocessed before
# subsetting the CASIA HWDB1.1 data set
import sys

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

import utils

if len(sys.argv) != 2:
    print 'Usage: %s gnt_dirpath' % sys.argv[0]
    exit()

gnt_dirpath = sys.argv[1]

for i, (bitmap, tagcode) in enumerate(utils.read_gnt_in_directory(gnt_dirpath)):
    print utils.tagcode_to_unicode(tagcode).encode('utf-8')  # wrong terminal encoding = garbage

    proc_bitmap = utils.normalize_bitmap(bitmap)
    proc_bitmap = utils.preprocess_bitmap(proc_bitmap)

    plt.subplot(121)
    plt.imshow(bitmap, cmap=cm.Greys_r)
    plt.subplot(122)
    plt.imshow(np.squeeze(proc_bitmap, axis=0), cmap=cm.Greys_r)
    plt.show()

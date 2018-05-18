#!/usr/bin/env python
from __future__ import print_function

import sys

import h5py

import utils
from utils import TRN_SIZE, TST_SIZE

if len(sys.argv) != 3:
    print('Usage: %s trn_dirpath tst_dirpath' % sys.argv[0]) 
    sys.exit(1)

trn_dirpath = sys.argv[1]
tst_dirpath = sys.argv[2]

def run():
    with h5py.File('HWDB1.1.hdf5', 'w') as f:
        for name, size, dirpath in [('trn', TRN_SIZE, trn_dirpath), ('tst', TST_SIZE, tst_dirpath)]:
            print('Converting \'%s\'...' % name)

            grp = f.create_group(name)
            dset_bitmap  = grp.create_dataset('bitmap',  (size, 64, 64, 1), dtype='uint8')
            dset_tagcode = grp.create_dataset('tagcode', (size, 1),         dtype='uint16')
            sample_num = 0

            for i, (bitmap, tagcode) in enumerate(utils.read_gnt_in_directory(dirpath)):
                dset_bitmap[i]  = utils.normalize_bitmap(bitmap)
                dset_tagcode[i] = tagcode
                sample_num += 1
            print("Sample Number: {0}".format(sample_num))


if __name__ == "__main__":
    import time
    start_time = time.time()
    run()
    print("--- %s seconds ---" % (time.time() - start_time))

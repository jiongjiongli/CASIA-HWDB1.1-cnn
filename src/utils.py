from __future__ import print_function
import os
import struct

import numpy as np
import scipy.misc
import skimage.exposure

TRN_SIZE = 893306
TST_SIZE = 223991

def read_gnt_in_directory(gnt_dirpath):
    def samples(file_path, f):
        HEADER_SIZE = 10
        packed_length = f.read(4)

        while len(packed_length) == 4:
            length = struct.unpack("<I", packed_length)[0]
            raw_label = struct.unpack(">BB", f.read(2))
            width = struct.unpack("<H", f.read(2))[0]
            height = struct.unpack("<H", f.read(2))[0]
            raw_photo_bytes = f.read(height * width)
            if length != height * width + HEADER_SIZE or len(raw_photo_bytes) != height * width:
                print("Warning! {0} {1} {2} {3} {4} {5} Actual: {6} Expected: {7}".format(file_path, packed_length, 
                    length, raw_label, height, width, len(raw_photo_bytes), height * width))
            else:
                photo_bytes = struct.unpack("{}B".format(height * width), raw_photo_bytes)
                bitmap = np.array(photo_bytes).reshape((height, width)).astype(np.uint8)
                tagcode = (raw_label[0] << 8) + (raw_label[1])
                yield bitmap, tagcode
            packed_length = f.read(4)

            
    for file_name in os.listdir(gnt_dirpath):
        if file_name.endswith('.gnt'):
            file_path = os.path.join(gnt_dirpath, file_name)
            with open(file_path, 'rb') as f:
                for bitmap, tagcode in samples(file_path, f):
                    yield bitmap, tagcode


def normalize_bitmap(bitmap):
    # pad the bitmap to make it squared
    pad_size = abs(bitmap.shape[0]-bitmap.shape[1]) // 2
    if bitmap.shape[0] < bitmap.shape[1]:
        pad_dims = ((pad_size, pad_size), (0, 0))
    else:
        pad_dims = ((0, 0), (pad_size, pad_size))
    bitmap = np.lib.pad(bitmap, pad_dims, mode='constant', constant_values=255)

    # rescale and add empty border
    bitmap = scipy.misc.imresize(bitmap, (64 - 4*2, 64 - 4*2))
    bitmap = np.lib.pad(bitmap, ((4, 4), (4, 4)), mode='constant', constant_values=255)
    assert bitmap.shape == (64, 64)

    bitmap = np.expand_dims(bitmap, axis= -1)
    assert bitmap.shape == (64, 64, 1)
    return bitmap

def preprocess_bitmap(bitmap):
    # contrast stretching
    p2, p98 = np.percentile(bitmap, (2, 98))
    assert abs(p2-p98) > 10
    bitmap = skimage.exposure.rescale_intensity(bitmap, in_range=(p2, p98))

    # from skimage.filters import threshold_otsu
    # thresh = threshold_otsu(bitmap)
    # bitmap = bitmap > thresh
    return bitmap


def tagcode_to_unicode(tagcode):
    return struct.pack('>H', tagcode).decode('gb2312')

def unicode_to_tagcode(tagcode_unicode):
    return struct.unpack('>H', tagcode_unicode.encode('gb2312'))[0]

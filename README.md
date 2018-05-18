# CASIA-HWDB1.1-cnn
This repository contains our experiments with the deep learning library [Keras](http://keras.io/) and a subset of the [CASIA-HWDB1.1](http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html) data set. The code here provided implements a convolutional neural network with test set accuracy greater than 95%. The network configuration is a simplified version of the one described in [Deep Convolutional Network for Handwritten Chinese Character Recognition](http://yuhao.im/files/Zhang_CNNChar.pdf) by Yuhao Zhang. No attempt was made to improve the accuracy of the model since we just wanted to play with convolutional networks and deep learning libraries.

Alessandro and Francesco
This code was last testd on a virtual machine with i7-5557U CPU @ 3.10GHz × 2 (no GPU), and 4GB memory.
The training step took 22 hours.
## Requisites
Prepare environment following steps in README-ENV.md
```

## Usage
In the releases section we uploaded a (zipped) [subset](https://github.com/jiongjiongli/CASIA-HWDB1.1-cnn/download/HWDB1.1subset.hdf5.zip) of the CASIA-HWDB1.1 data set, the [network model](https://github.com/jiongjiongli/CASIA-HWDB1.1-cnn/download/model.json), [network weights](https://github.com/jiongjiongli/CASIA-HWDB1.1-cnn/download/weights.hdf5) and [some classifications](https://github.com/jiongjiongli/CASIA-HWDB1.1-cnn/download/results.html), all generated following the steps below. If you use our subset, start from step 3.

0. Download the CASIA-HWDB1.1 data set from the official locations ([HWDB1.1trn_gnt_P1.zip](http://www.nlpr.ia.ac.cn/databases/Download/feature_data/HWDB1.1trn_gnt_P1.zip) (901 MB), ([HWDB1.1trn_gnt_P2.zip](http://www.nlpr.ia.ac.cn/databases/Download/feature_data/HWDB1.1trn_gnt_P2.zip) (947 MB) (Note: ([HWDB1.1trn_gnt.zip](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn_gnt.zip) (1873 MB) is broken) and [HWDB1.1tst_gnt.zip](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst_gnt.zip) (471 MB)) and unzip it (it is required to decompress an archive in ALZ format):
```
$ unzip HWDB1.1trn_gnt_P1.zip
[...]
$ unzip HWDB1.1trn_gnt_P2.zip
[...]
$ mkdir HWDB1.1trn_gnt
$ mv *.gnt HWDB1.1trn_gnt/
$ unzip HWDB1.1tst_gnt.zip
Archive:  HWDB1.1tst_gnt.zip
  inflating: 1289-c.gnt
  inflating: 1290-c.gnt
  [...]
$ mkdir HWDB1.1tst_gnt
$ mv *.gnt HWDB1.1tst_gnt/
```
1. Convert the data set into the HDF5 binary data format:
```
$ python 1-gnt_to_dataset.py HWDB1.1trn_gnt/ HWDB1.1tst_gnt/
Converting 'trn'...
Converting 'tst'...
```
2. Extract from the HDF5 data set a subset of 200 classes of characters:
```
$ python 2-dataset_to_subset.py HWDB1.1.hdf5
Subsetting 'trn'...
Subsetting 'tst'...
```
3. Train the network on the subset:
```
$ python 3-train_subset.py HWDB1.1subset.hdf5
[...]
Using Tensorflow backend.
Test score: 0.20873856527750181
Test accuracy: 0.9578136770737423
--- 79944.11841607094 seconds ---
```
4. (Optional) Generate a report of some classifications:
```
$ python 4-draw_results.py HWDB1.1subset.hdf5 model.json weights.hdf5
Using TensorFlow backend.
2018-05-17 23:49:04.103902: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
Evaluating the network on the test set...
Test score: 0.20873856527750181
Test accuracy: 0.9578136770737423
Extracting some results...
Sample number: 11947
--- 101.42111706733704 seconds ---
```
```
5. (Optional) View results in results.html
```
<img src="/dowload/results.png" alt="Results"/>
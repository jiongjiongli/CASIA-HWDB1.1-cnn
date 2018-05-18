# Environment

OS: Ubuntu 18.04

## Steps

1. Add user to sudo with visudo

2. Install Anaconda
```
$ Anaconda3-5.1.0-Linux-x86_64.sh
  Do you wish the installer to prepend the Anaconda3 install location
  to PATH in your /home/ai/.bashrc ? [yes|no]
  [yes] >>>
  
  Thank you for installing Anaconda3!
```
3. Create an envronment
```
$ conda create -n py34 python=3.4 anaconda
```
4. Activate environment
```
$ source activate py34
```
5. Install opencv (optional)
```
$ conda install opencv
```
6. Install tensorflow
```
$ onda install -c conda-forge tensorflow
```

from scipy.misc import imread, imresize, imsave
from scipy.optimize import fmin_l_bfgs_b
from sklearn.preprocessing import normalize
import numpy as np 
import time
import os
import argparse
import h5py

from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, ZeroPadding2D, AveragePooling2D
from keras import backend as K 

args = parser.parse_args()
base_image_path = args.base_image_path
style_reference_image_path = args.style_reference_image_path
result_prefix = args.result_prefix

weights_path = r"vgg16_weights.h5"

 rescale_image = strToBool(args.rescale_image)
 maintain_aspect_ratio = strToBool(args.maintain_aspect_ratio)

 total_variation_weight = args_tv_weight
 style_weight = args.style_weight * args.style_scale
 content_weight = args.content_weight
# You can change this supervision_mode between 'phi' and 'xy'. See the assinment pdf for more details.
supervision_mode = 'phi'

# imports
import math
import zipfile
import os
from io import BytesIO

import matplotlib.pyplot as plt

import IPython.display

from tqdm.notebook import tqdm

import PIL

import numpy as np

import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import os
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from collections import Counter

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

data_dir = Path("D:\freelancer_projects\captcha\design_captcha")
print(data_dir)
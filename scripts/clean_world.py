import os
import shutil

import distutils.core

root = 'C:\Users\esgee\Projects\kap'

source = os.path.join(root,"test")
destination = os.path.join(root, "_world")

shutil.rmtree(os.path.join(root,"_world"))
os.makedirs(os.path.join(root,"_world"))

distutils.dir_util.copy_tree(source, destination)
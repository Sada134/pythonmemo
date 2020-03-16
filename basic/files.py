#!/usr/bin/env python
#coding: UTF-8

import glob
import os
import shutil
from distutils.dir_util import copy_tree


# ファイル名のリストを取得
file_list =glob.glob("./*")

for fn in file_list:
    path, ext = os.path.splitext(fn) # 拡張子とファイル名に分離
    alterd_fn = fn
    # os.rename(alterd_fn, path + ".csv")
    
    print('full: %s' % fn)
    print('path: %s' % path)
    print('ext: %s' % ext)


# ディレクトリ有無を確認して、なければ作成
if not os.path.exists("./copied"):
    os.mkdir("./copied")

# ファイルコピー
shutil.copy('./files.py', './copied/files_copied.py')

# ディレクトリごとコピー
copy_tree('./copied','./copied_duplicated')

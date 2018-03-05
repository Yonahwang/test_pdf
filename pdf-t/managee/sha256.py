#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import os
import pickle

files =r"/home/yonah/PDFdata/pdfnormal"
pathDir =  os.listdir(files)

#downf = open("tsha_pdf_83442.txt",'wb')
file_sha256 = []
for file in pathDir:
    f = files + "/" + file
    fr = open(f, 'rb')
    sh = hashlib.sha256()
    sh.update(fr.read())
    file_sha256.append(sh.hexdigest())
    #downf.write(sh.hexdigest() + '\n')

pickle.dump(file_sha256,open('pdf_sha256.pkl','wb'))

#downf.close()

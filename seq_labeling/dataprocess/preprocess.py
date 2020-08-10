#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 上午9:10
# @Author  : Tahoe
# @Email   : wangtaihao12@163.com
# @File    : preprocess.py
# @Software: PyCharm


new_train = []
raw_train = '../data/data_dev.txt'
raws_text, raws_label = [], []
with open(raw_train, 'r', encoding='utf-8') as opf:
    for line in opf:
        ls = line.strip().split(' ')
        word, tag = ls[0], ls[-1]
        raws_text.append(word)
        if tag == 'B-PER':
            tag = 'B'
        elif tag == 'I-PER':
            tag = 'I'
        raws_label.append(tag)

seq_len = 256
cont = len(raws_label)//seq_len
for i in range(cont):
    new_train.append(''.join(raws_text[256*i:256*(i+1)])+'\t'+''.join(raws_label[256*i:256*(i+1)]))

with open('../data/dev.txt','wb') as wrf :
    for sentence in new_train:
        wrf.write((sentence+'\n').encode())
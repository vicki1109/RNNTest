#!/usr/bin/env python
from __future__ import print_function

import logging
import os.path
import six
import sys

from gensim.corpora import WikiCorpus

if __name__ =='__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
#打印时间、日志级别、日志信息
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ''.join(sys.argv))

#check and process input arguments
    if len(sys.argv)!=3:
        print("Using:python process_wiki.py enwiki.xxx.xml.bz2 wiki.en.text")
        sys.exit(1)
    inp,outp = sys.argv[1:3]
    space = " "
    i = 0

    output = open(outp,'w')
    #lemmatize设为False是不使用pattern模块来进行英文单词的词干化处理，处理速度很慢
    wiki = WikiCorpus(inp,lemmatize=False,dictionary={})
    for text in wiki.get_texts():
        if six.PY3:
            output.write(b''.join(text))




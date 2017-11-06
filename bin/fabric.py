#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author = "susu"
import os
import sys
basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
from core import main
if __name__ == '__main__':
    main.run()